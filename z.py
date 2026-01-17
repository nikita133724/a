import asyncio
from pyppeteer import launch
from pathlib import Path

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

async def main():
    # Запускаем headless браузер
    browser = await launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
    page = await browser.newPage()
    
    print(f"[INFO] Opening {URL} ...")
    await page.goto(URL, waitUntil='networkidle2')  # ждем пока JS загрузится
    await page.waitForTimeout(3000)  # дополнительные 3 секунды на загрузку динамики
    
    html = await page.content()
    OUT_FILE.write_text(html, encoding="utf-8")
    print(f"[OK] HTML saved to {OUT_FILE.resolve()}")
    
    await browser.close()

# Запуск
asyncio.get_event_loop().run_until_complete(main())