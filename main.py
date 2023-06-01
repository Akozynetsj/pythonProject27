import requests
from bs4 import BeautifulSoup

def get_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    for table in tables:
        print(table.prettify())
url = 'https://www.example.com'
get_tables(url)
