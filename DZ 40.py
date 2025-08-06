import requests
from bs4 import BeautifulSoup

url = "https://xn--e1afka0abm4b.xn--p1ai/krsk/nabori"

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find("article",class_="product-card")
name = soup.find("h2", class_="product-name").text.strip()
price = data.find("div", class_="g-button-text")
print(price)