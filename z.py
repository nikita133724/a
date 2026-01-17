import subprocess
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

# -------------------------------
# Устанавливаем системные зависимости
# -------------------------------
def install_system_dependencies():
    print("[INFO] Installing system dependencies for Chromium...")
    deps = [
        "libnss3","libatk1.0-0","libatk-bridge2.0-0","libcups2","libdrm2",
        "libxkbcommon0","libxcomposite1","libxdamage1","libxrandr2","libgbm1",
        "libpango-1.0-0","libpangocairo-1.0-0","libx11-6","libxext6",
        "libxfixes3","libxrender1","libxcb1","libxcb-shm0","libxcb-dri2-0",
        "libgtk-3-0","libasound2","fonts-liberation","libxss1","lsb-release"
    ]
    subprocess.run(["sudo", "apt", "update"], check=True)
    for pkg in deps:
        print(f"[INFO] Installing {pkg}...")
        subprocess.run(["sudo", "apt", "install", "-y", pkg], check=False)  # продолжаем даже если что-то не установилось
    print("[OK] System dependencies installed.")

# -------------------------------
# Устанавливаем Playwright и Chromium
# -------------------------------
def install_playwright():
    print("[INFO] Installing Python packages...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
    print("[INFO] Installing Chromium for Playwright...")
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    print("[OK] Playwright and Chromium installed.")

# -------------------------------
# Получаем HTML страницы
# -------------------------------
def fetch_page_html():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
        page = browser.new_page()
        print(f"[INFO] Opening {URL} ...")
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(5000)  # ждем 5 секунд, чтобы страница полностью загрузилась
        html = page.content()
        OUT_FILE.write_text(html, encoding="utf-8")
        print(f"[OK] HTML saved to {OUT_FILE.resolve()}")
        browser.close()

# -------------------------------
# Главная функция
# -------------------------------
def main():
    install_system_dependencies()
    install_playwright()
    fetch_page_html()

if __name__ == "__main__":
    main()