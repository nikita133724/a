from pathlib import Path
from playwright.sync_api import sync_playwright
import subprocess

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

# Минимальные зависимости для Codespaces
subprocess.run(["sudo", "apt", "update"], check=True)
subprocess.run([
    "sudo", "apt", "install", "-y",
    "libnss3", "libatk1.0-0", "libatk-bridge2.0-0", "libcups2",
    "libdrm2", "libxkbcommon0", "libxcomposite1", "libxdamage1",
    "libxrandr2", "libgbm1", "libpango-1.0-0", "libpangocairo-1.0-0",
    "libx11-6", "libxext6", "libxfixes3", "libxrender1", "libxcb1",
    "libxcb-shm0", "libxcb-dri2-0", "libgtk-3-0", "libasound2"
], check=False)

# Устанавливаем playwright
subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "pip"], check=True)
subprocess.run(["python3", "-m", "pip", "install", "playwright"], check=True)
subprocess.run(["python3", "-m", "playwright", "install", "chromium"], check=True)

# Headless fetch
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(5000)
    OUT_FILE.write_text(page.content(), encoding="utf-8")
    print(f"[OK] HTML saved to {OUT_FILE.resolve()}")
    browser.close()