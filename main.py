import requests
from bs4 import BeautifulSoup

def get_h1_with_attributes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h1 = soup.find('h1')
    if h1:
        attributes = h1.attrs
        print(f"<h1> attributes: {attributes}")
    else:
        print("No <h1> element found.")

url = 'https://www.example.com'
get_h1_with_attributes(url)
