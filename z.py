import asyncio
from pyppeteer import launch
from pathlib import Path

URL = "https://csgoyz.run/raffles"
OUT_FILE = Path("raffles_dom.html")

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(URL)
    await page.waitForTimeout(5000)
    html = await page.content()
    OUT_FILE.write_text(html, encoding="utf-8")
    await browser.close()
    print(f"[OK] HTML saved to {OUT_FILE.resolve()}")

asyncio.run(main())