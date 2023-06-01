import requests
from bs4 import BeautifulSoup

def get_h2_headings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h2_headings = soup.find_all('h2')
    for heading in h2_headings:
        print(heading.text)
url = 'https://www.example.com'
get_h2_headings(url)
