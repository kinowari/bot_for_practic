import requests
from bs4 import BeautifulSoup
#sankt_peterburg

mainHref = 'https://pogoda.mail.ru/prognoz/'
#city=input('Введите город на английском транслите, пример ''moskva'' >> ')

def getHtml(url):
    """Получение HTML"""
    r = requests.get(url).text
    return r

def getTemperature(url):
    content=BeautifulSoup(getHtml(mainHref+url+'/'))
    temperatura= 'Температура прямо сейчас '+content.find('div', class_="information__content__temperature").text.strip('\n')
    feels=content.find('div',class_='information__content__additional__item').text.strip('\n')
    return temperatura+'\n'+feels

#print(getTemperature(mainHref+city+'/'))

