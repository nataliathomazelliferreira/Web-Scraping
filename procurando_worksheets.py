import requests
from bs4 import BeautifulSoup

url = "https://agendaweb.org/grammar-exercises.html"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

links = soup.select("a")

file = open("worksheets.txt", "w", encoding="utf-8")

print("Worksheets encontrados:\n")

for link in links:
    titulo = link.get_text(strip=True)
    href = link.get("href")

    if titulo and href and "http" in href:
        print(f"{titulo} -> {href}")
        file.write(f"{titulo} -> {href}\n")

file.close()

print("\nLinks salvos em worksheets.txt")