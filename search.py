import requests, sys, webbrowser, os
from bs4 import BeautifulSoup


def value(valeurs):


    os.system('clear')

    rbi = requests.get('https://www.bing.com/search?q='+ valeurs)

    rbi.raise_for_status()

    souprbi = BeautifulSoup(rbi.text, 'html.parser')

    linkElementsrbi = souprbi.find_all('a')

    linkToOpen = min(100, len(linkElementsrbi))

    webbrowser.open_new_tab('https://loderi.com/'+ valeurs)
    webbrowser.open("https://who.is/whois/" + valeurs)
    webbrowser.open("https://www.youtube.com/results?search_query=" + valeurs)

    for i in range(linkToOpen):
        webbrowser.open('https://bing.com' + linkElementsrbi[i].get('href'))
        print('recherche en cour...')

