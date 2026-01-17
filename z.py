from playwright.sync_api import sync_playwright
from pathlib import Path

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

        # Ждём, пока SPA полностью отрисуется
        page.wait_for_timeout(5000)

        print("[INFO] Dumping HTML...")
        html = page.content()
        OUT_FILE.write_text(html, encoding="utf-8")

        print(f"[OK] HTML saved to {OUT_FILE.resolve()}")

        browser.close()

if __name__ == "__main__":
    main()
