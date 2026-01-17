import subprocess
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

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
        subprocess.run(["sudo", "apt", "install", "-y", pkg], check=False)
    print("[OK] System dependencies installed.")

def install_playwright():
    print("[INFO] Installing Playwright Python package...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
    print("[INFO] Installing Chromium for Playwright...")
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    print("[OK] Playwright and Chromium installed.")

def fetch_html():
    with sync_playwright() as p:
        print(f"[INFO] Launching headless Chromium to fetch {URL} ...")
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page()
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(5000)  # ждем JS
        html = page.content()
        OUT_FILE.write_text(html, encoding="utf-8")
        print(f"[OK] HTML saved to {OUT_FILE.resolve()}")
        browser.close()

def main():
    install_system_dependencies()
    install_playwright()
    fetch_html()

if __name__ == "__main__":
    main()