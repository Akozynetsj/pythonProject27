import requests
from bs4 import BeautifulSoup

def get_elements_with_class(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_=class_name)
    for element in elements:
        print(element)
url = 'https://www.example.com'
class_name = 'example-class'
get_elements_with_class(url, class_name)
