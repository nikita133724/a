import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

# -------------------------------
# 1. Устанавливаем системные зависимости для Chromium
# -------------------------------
def install_dependencies():
    print("[INFO] Installing system dependencies for Chromium...")
    deps = [
        "libnss3",
        "libatk1.0-0",
        "libatk-bridge2.0-0",
        "libcups2",
        "libdrm2",
        "libxkbcommon0",
        "libxcomposite1",
        "libxdamage1",
        "libxrandr2",
        "libgbm1",
        "libpango-1.0-0",
        "libpangocairo-1.0-0",
        "libasound2",
        "libxshmfence1",
        "libgtk-3-0",
        "libx11-xcb1",
        "libxcb-dri3-0",
        "libx11-6",
        "libxext6",
        "libxfixes3",
        "libxrender1",
        "libxcb1",
        "libxcb-shm0",
        "libxcb-dri2-0"
    ]
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "install", "-y"] + deps, check=True)
    print("[OK] Dependencies installed.")

# -------------------------------
# 2. Запускаем Playwright и сохраняем HTML
# -------------------------------
def main():
    install_dependencies()

    # Скачиваем Chromium через Playwright (если не скачан)
    subprocess.run(["python3", "-m", "playwright", "install", "chromium"], check=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )
        page = browser.new_page()

        print("[INFO] Opening page...")
        page.goto(URL, wait_until="networkidle")

        # Ждём, пока SPA полностью отрисуется
        page.wait_for_timeout(5000)

        print("[INFO] Dumping HTML...")
        html = page.content()
        OUT_FILE.write_text(html, encoding="utf-8")

        print(f"[OK] HTML saved to {OUT_FILE.resolve()}")

        browser.close()

if __name__ == "__main__":
    main()