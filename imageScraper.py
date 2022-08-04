import requests
from bs4 import BeautifulSoup

URL = input('Please enter a url \n(If using CMD and not Powershell paste is CTRL+SHIFT+V)\n--> ')

r = requests.get(URL) # retrieves the page data
soup = BeautifulSoup(r.content, 'html5lib') #converts raw data to DOM

for row in soup.findAll('div', attrs = {'class' : 'Panel-img'}): #loops through all mentions of the css class panel-img
    image = {} #empty obj to store data in
    image['source'] = row.img['src'] #attaches source of each image to obj
    image['alt'] = row.img['alt'] #attaches alt text of each image to obj
    print(image)

exit = input ("press any key to exit") # this is needed so the command line doesn't immediately close once the script has run