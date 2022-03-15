from rich import print
import random as rd
import requests
import time
import os

limpar = 'clear'

lista = ['blue', 'yellow', 'cyan', 'white', 'red', 'green']

def Moeda():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    site = requests.get(url)
    info_moeda = site.json()

    cotacao = info_moeda['USDBRL']['bid']

    for i in range(1,9999999999):
        qq = rd.choice(lista)
        print(
            f'[{qq}]**************************\n'
            '*                        *\n'
            '*    Cotação do Dolar    *\n'
            '*                        *\n'
            '*                        *\n'
            '**************************[/]')

        print(f'\n\n{i} - Cotação atual do dolar: {cotacao[:4]}')

        if cotacao > '5.13':
            print(
                f'\nO dolar subiu para: {cotacao[:4]}'
                )
            time.sleep(1)
            os.system(limpar)

        elif cotacao < '5.12':
            print(
                f'\nO dolar caiu para: {cotacao[:4]}'
                )
            time.sleep(1)
            os.system(limpar)

Moeda()