import os
from requests_html import HTMLSession

# Берём URL из переменной окружения или ставим дефолт
url = os.environ.get("TARGET_URL", "https://csgoyz.run/raffles")

session = HTMLSession()

print(f"[INFO]: Открываем {url}")

# Получаем страницу
r = session.get(url)

# Рендерим JS (по умолчанию timeout=8 секунд, можно увеличить)
r.html.render(timeout=20)  

# Выводим финальный HTML в логи Render
print("[HTML]:", r.html.html)