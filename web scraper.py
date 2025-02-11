import requests
from bs4 import BeautifulSoup

url = input("Introduce la URL: ") 

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"<h1>: {soup.find_all('h1')}")
    print(f"<h2>: {soup.find_all('h2')}")
    print(f"<h3>: {soup.find_all('h3')}")
else:
    print("Error")