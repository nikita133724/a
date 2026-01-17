import sys
import subprocess
from pathlib import Path

def run(cmd):
    print(f"[RUN] {' '.join(cmd)}")
    subprocess.check_call(cmd)

# 1. Установка playwright если нет
try:
    import playwright  # noqa
except ImportError:
    print("[INFO] playwright not found, installing...")
    run([sys.executable, "-m", "pip", "install", "playwright"])

# 2. Установка chromium (один раз)
try:
    from playwright.sync_api import sync_playwright
except Exception:
    print("[INFO] Installing Chromium...")
    run([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.sync_api import sync_playwright

# 3. Запуск браузера и дамп HTML
URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

def main():
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

        # даём SPA дорендериться
        page.wait_for_timeout(5000)

        print("[INFO] Dumping DOM...")
        html = page.content()
        OUT_FILE.write_text(html, encoding="utf-8")

        print(f"[OK] Saved to {OUT_FILE.resolve()}")
        browser.close()

if __name__ == "__main__":
    main()
