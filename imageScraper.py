import requests
from bs4 import BeautifulSoup



URL = input('Please enter a url \n(If using CMD and not Powershell paste is CTRL+SHIFT+V)\n--> ')

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

images = []

for row in soup.findAll('div', attrs = {'class' : 'Panel-img'}):
    image = {}
    image['source'] = row.img['src']
    image['alt'] = row.img['alt']
    images.append(image)
    print(image)
