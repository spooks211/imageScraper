import requests
from bs4 import BeautifulSoup

while True:
    URL = input('Please enter a url \n---> ')

    r = requests.get(URL) # retrieves the raw page data
    soup = BeautifulSoup(r.content, 'html5lib') #converts raw data to DOM

    for row in soup.findAll('div', attrs = {'class' : 'Hero-figure'}): #hero images use a different class name, this is for that
        hero = {}
        hero['hero source'] = row.img['src']
        hero['hero alt'] = row.img['alt']
        print(hero)

    for row in soup.findAll('div', attrs = {'class' : 'Panel-img'}): #loops through all mentions of the css class panel-img (cards etc)
        image = {} #empty object to store source and alt in
        image['source'] = row.img['src'] #attaches source of each image to object
        image['alt'] = row.img['alt'] #attaches alt text of each image to object
        print(image)

    exitOrRunAgain = input ("Would you like to run the script again? y/n \n IF YOU WANT TO KEEP THE DATA ON SCREEN TO WORK ON IT DO NOT PRESS ANYTHING UNTIL YOU'RE DONE\n---> ")
    exitOrRunAgain = exitOrRunAgain.lower()

    if exitOrRunAgain == 'y':
        continue

    elif exitOrRunAgain == 'n':
        break

    else:
        break