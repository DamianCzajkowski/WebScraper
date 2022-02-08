import requests

web_page = requests.get("https://www.x-kom.pl/p/707158-smartfon-telefon-samsung-galaxy-s21-fe-5g-fan-edition-grey.html")
print(str(web_page.content))
