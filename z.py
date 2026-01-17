import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

# -------------------------------
# Устанавливаем системные зависимости, игнорируем отсутствующие
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
        "libx11-6",
        "libxext6",
        "libxfixes3",
        "libxrender1",
        "libxcb1",
        "libxcb-shm0",
        "libxcb-dri2-0",
        "libgtk-3-0"
    ]
    subprocess.run(["sudo", "apt", "update"], check=True)
    for pkg in deps:
        print(f"[INFO] Installing {pkg}...")
        subprocess.run(["sudo", "apt", "install", "-y", pkg], check=False)  # check=False пропускает ошибки
    print("[OK] Dependencies installed (skipped missing packages if any).")

# -------------------------------
# Сохраняем HTML страницы
# -------------------------------
def main():
    install_dependencies()
    subprocess.run(["python3", "-m", "playwright", "install", "chromium"], check=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page()
        print("[INFO] Opening page...")
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(5000)
        html = page.content()
        OUT_FILE.write_text(html, encoding="utf-8")
        print(f"[OK] HTML saved to {OUT_FILE.resolve()}")
        browser.close()

if __name__ == "__main__":
    main()