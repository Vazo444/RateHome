import requests
from bs4 import BeautifulSoup
import json

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
}

banks = []

def acbaBank():
    sesion = requests.Session()
    response = sesion.get(url='https://www.acba.am/' , headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    acba = soup.findAll('div', {'class': 'price-num'})
    
    banks.append({
        'USD': [acba[0].text, x := acba[1].text.replace('\t' , '').replace('\n' , '')],
        'EUR': [acba[3].text, x := acba[4].text.replace('\t' , '').replace('\n' , '')],
        'RUB': [acba[6].text, x := acba[7].text.replace('\t' , '').replace('\n' , '')],
        'GBP': [acba[9].text, x := acba[10].text.replace('\t' , '').replace('\n' , '')],
    })


def yuniBank():
    sesion = requests.Session()
    response = sesion.get(url='https://www.unibank.am/hy/' , headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    yuni = soup.findAll('span')
    
    banks.append({
        'USD': [yuni[6].text, x := yuni[7].text.replace('\t' , '').replace('\n' , '')],
        'EUR': [yuni[9].text, x := yuni[10].text.replace('\t' , '').replace('\n' , '')],
        'RUB': [yuni[12].text, x := yuni[13].text.replace('\t' , '').replace('\n' , '')],
        'GBP': [yuni[15].text, x := yuni[16].text.replace('\t' , '').replace('\n' , '')],
    })


def hayEconom():
    sesion = requests.Session()
    response = sesion.get(url='https://www.aeb.am/' , headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    econom = soup.findAll('td')
    
    banks.append({
        'USD': [econom[13].text, x := econom[14].text.replace('\t' , '').replace('\n' , '')],
        'EUR': [econom[17].text, x := econom[18].text.replace('\t' , '').replace('\n' , '')],
        'RUB': [econom[21].text, x := econom[22].text.replace('\t' , '').replace('\n' , '')],
        'GBP': [econom[25].text, x := econom[26].text.replace('\t' , '').replace('\n' , '')],
    })


def ameria():
    sesion = requests.Session()
    response = sesion.get(url='https://ameriabank.am/ru/' , headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    ameria = soup.findAll('td', {'align': 'right'})
    
    banks.append({
        'USD': [ameria[0].text, x := ameria[1].text.replace('\t' , '').replace('\n' , '')],
        'EUR': [ameria[4].text, x := ameria[5].text.replace('\t' , '').replace('\n' , '')],
        'RUB': [ameria[8].text, x := ameria[9].text.replace('\t' , '').replace('\n' , '')],
        'GBP': [ameria[16].text, x := ameria[17].text.replace('\t' , '').replace('\n' , '')],
    })

ameria()

def ararat():
    sesion = requests.Session()
    response = sesion.get(url='https://www.araratbank.am/hy/' , headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    ararat = soup.findAll('td', {'class': 'exchange__table-cell fs20'})
    
    banks.append({
        'USD': [ararat[0].text, x := ararat[1].text.replace('\t' , '').replace('\n' , '')],
        'EUR': [ararat[3].text, x := ararat[4].text.replace('\t' , '').replace('\n' , '')],
        'RUB': [ararat[6].text, x := ararat[7].text.replace('\t' , '').replace('\n' , '')],
        'GBP': [ararat[9].text, x := ararat[10].text.replace('\t' , '').replace('\n' , '')],
    })


def aydi():
    sesion = requests.Session()
    response = sesion.get(url='https://idbank.am/rates/' , headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    aydi = soup.findAll('div', {'class': 'm-exchange__table-cell'})
    
    banks.append({
        'USD': [aydi[4].text.replace('\t' , '').replace('\n' , ''), x := aydi[5].text.replace('\t' , '').replace('\n' , '')],
        'EUR': [aydi[7].text.replace('\t' , '').replace('\n' , ''), x := aydi[8].text.replace('\t' , '').replace('\n' , '')],
        'RUB': [aydi[10].text.replace('\t' , '').replace('\n' , ''), x := aydi[11].text.replace('\t' , '').replace('\n' , '')],
        'GBP': [aydi[13].text.replace('\t' , '').replace('\n' , ''), x := aydi[14].text.replace('\t' , '').replace('\n' , '')],
    })


def convers():
    sesion = requests.Session()
    response = sesion.get(url='https://conversebank.am/ru/' , headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    convers = soup.findAll('td', {'class': 'currency_num'})
    convers1 = soup.findAll('td', {'class': 'currency_num_1'})
    
    banks.append({
        'USD': [convers[1].text.replace('\t' , '').replace('\n' , ''), x := convers1[1].text.replace('\t' , '').replace('\n' , '')],
        'EUR': [convers[2].text.replace('\t' , '').replace('\n' , ''), x := convers1[2].text.replace('\t' , '').replace('\n' , '')],
        'RUB': [convers[4].text.replace('\t' , '').replace('\n' , ''), x := convers1[4].text.replace('\t' , '').replace('\n' , '')],
        'GBP': [convers[3].text.replace('\t' , '').replace('\n' , ''), x := convers1[3].text.replace('\t' , '').replace('\n' , '')],
    })


def vtb():
    sesion = requests.Session()
    response = sesion.get(url='https://www.vtb.am/' , headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    vtb = soup.findAll('span', {'class': 'currency-item'})
    
    banks.append({
        'USD': [vtb[0].text.replace('\n' , ''), x := vtb[1].text.replace('\t' , '').replace('\n' , '')],
        'EUR': [vtb[2].text.replace('\t' , '').replace('\n' , ''), x := vtb[3].text.replace('\t' , '').replace('\n' , '')],
        'RUB': [vtb[4].text.replace('\t' , '').replace('\n' , ''), x := vtb[5].text.replace('\t' , '').replace('\n' , '')],
    })







def main():
    acbaBank()  
    yuniBank()
    hayEconom()
    ararat()
    aydi()
    convers()
    vtb()
    with open('rate.json' , 'w' , encoding='UTF-8') as file:
        json.dump(banks , file , indent=3 , ensure_ascii=False)






if __name__ == '__main__':
    main()




















# import json

# with open('./info.json' , 'r' , encoding='UTF-8') as file:
#     result = json.load(file)


# python today web parsing scrapping