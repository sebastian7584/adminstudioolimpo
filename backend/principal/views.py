from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .models import Account, Master, Earning, Period
from .serializers import CountrySerializer
import requests  #Importamos la librería requests
from datetime import date, datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyrebase
from datetime import datetime, timedelta
import json
import time
import pathlib
import pandas
from os import remove
import os
import numpy as np
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Create your views here.

@api_view(["GET"])
def selenium(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://python.org")
    mensaje = driver.title
    driver.close()
    return Response({'detail': mensaje})

@api_view(["GET"])
def asignarPagina(request):
    numero = Account.objects.filter(code_user=None).first()
    print(numero.code_user)
    numero = numero.id
    return redirect(f'/api/v1.0/account/{numero}/')


@api_view(["POST"])
def cargarDataUnidad(request):
    master = request.data['master']
    cuenta = request.data['cuenta']
    dia = request.data['dia']
    mes = request.data['mes']
    año = request.data['año']
    valor = request.data['valor']
    GuardarEstadistica(master, cuenta, dia, mes, año, valor).save()
        
    return Response({'detail': "no"})


@api_view(["GET"])
def cargarPaginas(request, dia, mes, año):
    cargar = CargarPaginas(dia, mes, año)
    cargar.chaturbate()
    cargar.stripchat()
    cargar.bonga()
    cargar.flirt4Free()
    cargar.streamate()
    resultado = cargar.resultado
    return Response(resultado)

@api_view(['POST'])
def chaturbate(request):
    dia = request.data['dia']
    mes = request.data['mes']
    año = request.data['año']
    cargar = CargarPaginas(dia, mes, año)
    cargar.chaturbate()
    resultado = cargar.resultado
    return Response(resultado)

@api_view(['POST'])
def stripchat(request):
    dia = request.data['dia']
    mes = request.data['mes']
    año = request.data['año']
    cargar = CargarPaginas(dia, mes, año)
    cargar.stripchat()
    resultado = cargar.resultado
    return Response(resultado)

@api_view(['POST'])
def bonga(request):
    dia = request.data['dia']
    mes = request.data['mes']
    año = request.data['año']
    cargar = CargarPaginas(dia, mes, año)
    cargar.bonga()
    resultado = cargar.resultado
    return Response(resultado)

@api_view(['POST'])
def flirt4free(request):
    dia = request.data['dia']
    mes = request.data['mes']
    año = request.data['año']
    cargar = CargarPaginas(dia, mes, año)
    cargar.flirt4Free()
    resultado = cargar.resultado
    return Response(resultado)

@api_view(['POST'])
def streamate(request):
    dia = request.data['dia']
    mes = request.data['mes']
    año = request.data['año']
    cargar = CargarPaginas(dia, mes, año)
    cargar.streamate()
    resultado = cargar.resultado
    return Response(resultado)

@api_view(['POST'])
def jasmin(request):
    dia = request.data['dia']
    mes = request.data['mes']
    año = request.data['año']
    cargar = CargarPaginas(dia, mes, año)
    cargar.jasmin()
    resultado = cargar.resultado
    return Response(resultado)

@api_view(['POST'])
def imlive(request):
    dia = request.data['dia']
    mes = request.data['mes']
    año = request.data['año']
    cargar = CargarPaginas(dia, mes, año)
    cargar.imlive()
    resultado = cargar.resultado
    return Response(resultado)






class GuardarEstadistica:

    def __init__(self, usernameMaster, usernameAccount, dia, mes, año, valor):
        self.usernameMaster = usernameMaster
        self.usernameAccount = usernameAccount
        self.dia = int(dia)
        self.mes = int(mes)
        self.año = int(año)
        self.valor = float(valor)

    def save(self):
        master = Master.objects.filter(username=self.usernameMaster).first()
        if master is not None:
            account = Account.objects.filter(username=self.usernameAccount, id_master=master).first()
            if account is None:
                nuevaCuenta = Account(username=self.usernameAccount, id_master=master)
                nuevaCuenta.save()
                account = Account.objects.filter(username=self.usernameAccount, id_master=master).first()
            periodo = 1 if self.dia < 16 else 2
            period = Period.objects.filter(year=self.año, mount=self.mes, period = periodo).first()
            if period is not None:
                print("entra a save")
                earning = Earning.objects.filter(date=self.dia, id_account=account, id_period=period).first()
                if earning is not None:
                    earning.amount = self.valor
                    earning.save()
                else:
                    nuevaEarning = Earning(
                        date= self.dia,
                        id_account= account,
                        amount= self.valor,
                        id_period= period,
                        percentage_studio= account.percentage_studio,
                        code_studio= account.code_studio,
                        percentage_user= account.percentage_user,
                        code_user= account.code_user,
                        percentage_substudio= account.percentage_substudio,
                        code_substudio= account.code_substudio,
                        percentage_referred= account.percentage_referred,
                        code_referred= account.code_referred,
                        percentage_other= account.percentage_other,
                        code_other= account.code_other,
                    )
                    nuevaEarning.save()
        return Response({'detail': "exitoso"})


class CargarPaginas:

    def __init__(self, dia, mes, año):
        self.resultado = {}
        self.dia = dia
        self.mes= mes
        self.año = año
        fecha_actual = datetime(int(año), int(mes), int(dia))
        nueva_fecha = fecha_actual + timedelta(days=1)
        self.dia2 = str(nueva_fecha.day)
        self.mes2 = str(nueva_fecha.month)
        self.año2 = str(nueva_fecha.year)
        if int(self.dia2) < 10 :
            self.dia2 ='0'+str(self.dia2)
        if int(self.mes2) < 10 :
            self.mes2 ='0'+str(self.mes2)
        firebaseConfig= {
            'apiKey': "AIzaSyDIVfFFVPeS-IItgh2ExPr2JPLCjh7gufI",
            'authDomain': "groovy-bonus-310519.firebaseapp.com",
            'databaseURL': "https://groovy-bonus-310519-default-rtdb.firebaseio.com",
            'projectId': "groovy-bonus-310519",
            'storageBucket': "groovy-bonus-310519.appspot.com",
            'messagingSenderId': "509390918244",
            'appId': "1:509390918244:web:84a5624f3ef04d23d20571",
            'measurementId': "G-DYE6S50CY9"
        }

        firebase=pyrebase.initialize_app(firebaseConfig)

        self.db=firebase.database()
    
    def scraping(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        tabla = self.soup.find('tbody')

        if tabla:
            filas = tabla.find_all('tr')
            datos_tabla = []
            for fila in filas:
                celdas = fila.find_all('td')
                datos_fila=[]
                for celda in celdas:
                    datos_fila.append(celda.get_text())
                datos_tabla.append(datos_fila)
        self.datos_tabla = datos_tabla

    
    def chaturbate(self):
        try:
            self.cargarChaturbate1()
            self.resultado['chaturbate1'] = 'exitosa'
        except:
            self.resultado['chaturbate1'] = 'fallo'
        try:
            self.cargarChaturbate2()
            self.resultado['chaturbate2'] = 'exitosa'
        except:
            self.resultado['chaturbate2'] = 'fallo'

    def cargarChaturbate1(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        db = self.db
        today = date.today()
        if int(dia) >15:
            quincena=2
            
        if int(dia) <16:
            quincena=1    
        URL = f'https://chaturbate.com/affiliates/apistats/?username=olimpostudio&token=H7tzkuPi7FXZgw8LAzuVGdwh&stats_breakdown=sub_account__username&campaign=&search_criteria=2&period=0&language=es&date={año}-{mes}-{dia}'
        # URL = 'https://es.chaturbate.com/affiliates/apistats/?username=olimpostudio&token=H7tzkuPi7FXZgw8LAzuVGdwh&stats_breakdown=sub_account__username&campaign=&search_criteria=2&period=0&date_day='+dia+'&date_month='+mes+'&date_year='+año+'&start_date_day=1&start_date_month=7&start_date_year=2021&end_date_day=15&end_date_month=7&end_date_year=2021' #configuramos la url
        #solicitamos la información y guardamos la respuesta en data.
        if dia != str(today.day):
            data = requests.get(URL) 
            
            data = data.json() #convertimos la respuesta en dict
            
            if data['stats'] == []: 
                print('dia sin estadisticas ch1')
            else:
                print(len(data['stats']))
                if  len(data['stats'])>1:
                    data = data['stats'][3]
                else: data = data['stats'][0]
                
                for i in range (0,len(data['rows'])):
                    db.child('chaturbate').child(data['rows'][i][0]).child(año+mes+str(quincena)).child(dia).set(data['rows'][i][2])
                    GuardarEstadistica('olimpostudio', data['rows'][i][0], dia, mes, año, data['rows'][i][2]).save()

        else: print('Solo se puede hasta dia anterior al actual')
    
    def cargarChaturbate2(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        db = self.db
        today = date.today()
        if int(dia) >15:
            quincena=2
            
        if int(dia) <16:
            quincena=1    
        URL = f'https://chaturbate.com/affiliates/apistats/?username=olimpostudioll&token=Cl9NSMn4hqMx6zT71z0vAIWu&stats_breakdown=sub_account__username&campaign=&search_criteria=2&period=0&language=es&date={año}-{mes}-{dia}'
        # URL = 'https://es.chaturbate.com/affiliates/apistats/?username=olimpostudioll&token=Cl9NSMn4hqMx6zT71z0vAIWu&stats_breakdown=sub_account__username&campaign=&search_criteria=2&period=0&date_day='+dia+'&date_month='+mes+'&date_year='+año+'&start_date_day=1&start_date_month=7&start_date_year=2021&end_date_day=15&end_date_month=7&end_date_year=2021' #configuramos la url
        #solicitamos la información y guardamos la respuesta en data.
        if dia != str(today.day):
            data = requests.get(URL) 

            data = data.json() #convertimos la respuesta en dict
        
            if data['stats'] == []: 
                print('dia sin estadisticas ch2')
            else:
                print(len(data['stats']))
                if  len(data['stats'])>1:
                    data = data['stats'][3]
                else: data = data['stats'][0]
                print(data)
                for i in range (0,len(data['rows'])):
                    db.child('chaturbate').child(data['rows'][i][0]).child(año+mes+str(quincena)).child(dia).set(data['rows'][i][2])
                    GuardarEstadistica('olimpostudioll', data['rows'][i][0], dia, mes, año, data['rows'][i][2]).save()

        else: print('Solo se puede hasta dia anterior al actual')

    def stripchat(self):
        try:
            self.cargarStripchat1()
            self.resultado['stripchat1'] = 'exitosa'
        except Exception as e:
            print(e)
            self.resultado['stripchat1'] = 'fallo'
        try:
            self.cargarStripchat2()
            self.resultado['stripchat2'] = 'exitosa'
        except:
            self.resultado['stripchat2'] = 'fallo'
        try:
            self.cargarStripchat3()
            self.resultado['stripchat3'] = 'exitosa'
        except:
            self.resultado['stripchat3'] = 'fallo'
    
    def cargarStripchat1(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        dia2 = self.dia2
        mes2 = self.mes2
        año2 = self.año2
        db = self.db
        if int(dia) >15:
            quincena=2
            
        if int(dia) <16:
            quincena=1    

        cookies = {
            'stripchat_com_firstVisit': '2023-04-16T14%3A40%3A49Z',
            'baseAmpl': '%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%221P9jHk2FjsHl_WPoF-K9SG%22%2C%22session_id%22%3A1682341128928%2C%22up%22%3A%7B%22page%22%3A%22index%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D',
            'alreadyVisited': '1',
            'amp_19a233': '1P9jHk2FjsHl_WPoF-K9SG.NDY1MDYxMQ==..1guplgqn0.1gupm4crp.0.70.70',
            'isVisitorsAgreementAccepted': '1',
            '_ga': 'GA1.2.1301892351.1681656050',
            '_gid': 'GA1.2.573934947.1682341133',
            'stripchat_com_sessionId': '804c4989241fdde38799d2a74543aba19b554b57219b1db01fffeceb1e7a',
            'stripchat_com_sessionRemember': '1',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/json',
            'Front-Version': '10.11.13',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://es.stripchat.com/studio-earnings',
            'Connection': 'keep-alive',
            'TE': 'trailers',
        }

        response = requests.get('https://es.stripchat.com/api/front/users/4650611/earnings?from='+año+'-'+mes+'-'+dia+'T05%3A00%3A00Z&until='+año2+'-'+mes2+'-'+dia2+'T04%3A59%3A59Z&uniq=1tkzc5a6jmiv0nhy', headers=headers, cookies=cookies)

        eq = json.loads(response.text)
        print(eq)
        
        for i in range (0, len(eq['earnings'])):
            db.child('stripchat').child(eq['earnings'][i]['username']).child(año+mes+str(quincena)).child(dia).set(eq['earnings'][i]['total']/20)
            GuardarEstadistica('olimpostudio-strip', eq['earnings'][i]['username'], dia, mes, año, eq['earnings'][i]['total']/20).save()
        
    def cargarStripchat2(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        dia2 = self.dia2
        mes2 = self.mes2
        año2 = self.año2
        db = self.db
        if int(dia) >15:
            quincena=2
            
        if int(dia) <16:
            quincena=1    

        cookies = {
            'stripchat_com_firstVisit': '2022-04-11T05%3A54%3A46Z',
            'guestWatchHistoryIds': '30042591',
            'guestFavoriteIds': '',
            'baseAmpl': '%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%22JPMfJl_A7RN_1SzE4UDCHU%22%2C%22session_id%22%3A1655395232266%2C%22up%22%3A%7B%22page%22%3A%22other%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D',
            'alreadyVisited': '1',
            'amp_19a233': 'JPMfJl_A7RN_1SzE4UDCHU.NzM2NzI5NjE=..1g5mjtaga.1g5mk055r.0.15.15',
            '_ga': 'GA1.2.926580397.1649656482',
            'sCashGuestId': 'e7b61ffc8ecf759de18319f7ddcb71d95c7b86116843c3e95f63345614bd5e81',
            'isVisitorsAgreementAccepted': '1',
            'guestWatchHistoryStartDate': '2022-04-16T17%3A39%3A37.780Z',
            '__cflb': '02DiuFntVtrkFMde1dj4khwPfLgZByWZi5m3READjJSur',
            '_gid': 'GA1.2.1388636281.1655395233',
            'stripchat_com_sessionId': 'e24ccf74344f90ec93bc9540c5731f14937b5045eff73793cbd02c977ec3',
            'stripchat_com_sessionRemember': '1',
            'userWatchHistoryIds': '30042591',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Front-Version': '10.34.13',
            'Alt-Used': 'es.stripchat.com',
            'Connection': 'keep-alive',
            'Referer': 'https://es.stripchat.com/studio-earnings',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'stripchat_com_firstVisit=2022-04-11T05%3A54%3A46Z; guestWatchHistoryIds=30042591; guestFavoriteIds=; baseAmpl=%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%22JPMfJl_A7RN_1SzE4UDCHU%22%2C%22session_id%22%3A1655395232266%2C%22up%22%3A%7B%22page%22%3A%22other%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D; alreadyVisited=1; amp_19a233=JPMfJl_A7RN_1SzE4UDCHU.NzM2NzI5NjE=..1g5mjtaga.1g5mk055r.0.15.15; _ga=GA1.2.926580397.1649656482; sCashGuestId=e7b61ffc8ecf759de18319f7ddcb71d95c7b86116843c3e95f63345614bd5e81; isVisitorsAgreementAccepted=1; guestWatchHistoryStartDate=2022-04-16T17%3A39%3A37.780Z; __cflb=02DiuFntVtrkFMde1dj4khwPfLgZByWZi5m3READjJSur; _gid=GA1.2.1388636281.1655395233; stripchat_com_sessionId=9e379ccdab10ddee5e93e5d7d65fae9f3b30b2583f0fb997e094099452d0; stripchat_com_sessionRemember=1; userWatchHistoryIds=30042591; _gat=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        params = {
            
            'from': ''+año+'-'+mes+'-'+dia+'T05:00:00Z',
            'until': año2+'-'+mes2+'-'+dia2+'T04:59:59Z',
            'uniq': 'mf193dw8tqgvoj76',
        }
        
        response = requests.get('https://es.stripchat.com/api/front/users/73672961/earnings', headers=headers, params=params, cookies=cookies)
        

        eq = json.loads(response.text)
        print(eq)

        for i in range (0, len(eq['earnings'])):
            db.child('stripchat').child(eq['earnings'][i]['username']).child(año+mes+str(quincena)).child(dia).set(eq['earnings'][i]['total']/20)
            GuardarEstadistica('olimpostudioll-strip', eq['earnings'][i]['username'], dia, mes, año, eq['earnings'][i]['total']/20).save()
        
    def cargarStripchat3(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        dia2 = self.dia2
        mes2 = self.mes2
        año2 = self.año2
        db = self.db
        if int(dia) >15:
            quincena=2
            
        if int(dia) <16:
            quincena=1    

        cookies = {
            'stripchat_com_firstVisit': '2023-03-22T19%3A09%3A18Z',
            'guestWatchHistoryIds': '',
            'guestFavoriteIds': '',
            'baseAmpl': '%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%22bzs9JfX8zJNqIQFfNqXXu6%22%2C%22session_id%22%3A1680363384926%2C%22up%22%3A%7B%22page%22%3A%22other%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D',
            'alreadyVisited': '1',
            'amp_19a233': 'bzs9JfX8zJNqIQFfNqXXu6.MTA4MjMzNjkx..1gsuncs2u.1gsuq5t2r.0.4a.4a',
            'isVisitorsAgreementAccepted': '1',
            'sCashGuestId': '5ef59394036cb1887c6eb7f4c70a93d3a7903546a2887c626e0a567b984a25aa',
            '_ga': 'GA1.1.1379988165.1679512158',
            '_gid': 'GA1.2.180793273.1680363386',
            'stripchat_com_sessionId': '8c2b28af15673f1eb4f616c84ce7f5ff6d949d2a2ccec2fe750a733ef3d4',
            'stripchat_com_sessionRemember': '1',
            'userWatchHistoryIds': '',
            'intercom-session-ylooj7fw': 'T2NNTXJhcllsME9GaHNndFVReFhLVERrQy9MdldHSlE5cUNwRXJOdW5sYmhYMWtsSTFsb0NBcFhPd1ducDJPdC0tek5TTjJSQ0plWVRMSzBYNC9PZnQwZz09--607a11795bca5e6b22659776ddfd1a2336f34f24',
            '_gat': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/json',
            'Front-Version': '10.11.13',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://es.stripchat.com/studio-earnings',
            'Connection': 'keep-alive',
            'TE': 'trailers',
        }

        response = requests.get('https://es.stripchat.com/api/front/users/108233691/earnings?from='+año+'-'+mes+'-'+dia+'T05%3A00%3A00Z&until='+año2+'-'+mes2+'-'+dia2+'T04%3A59%3A59Z&uniq=7htn1dkp4cxqv36w', headers=headers, cookies=cookies)

        eq = json.loads(response.text)
        print(eq)

        for i in range (0, len(eq['earnings'])):
            db.child('stripchat').child(eq['earnings'][i]['username']).child(año+mes+str(quincena)).child(dia).set(eq['earnings'][i]['total']/20)
            GuardarEstadistica('juantokens-strip', eq['earnings'][i]['username'], dia, mes, año, eq['earnings'][i]['total']/20).save()
    
    def bonga(self):
        try:
            self.cargarBonga1()
            self.resultado['bonga1'] = 'exitosa'
        except Exception as e:
            print(e)
            self.resultado['bonga1'] = 'fallo'
        
    def cargarBonga1(self):
        modelos=[
            'rachellsex',
            'ethan-jobs10',
            'Besparis-xx99',
            'noah-hot',
            'taty-natasha',
            'rosa-sexhot',
            'fetish-BDSM-3',
            'submissionfet',
            'proyectxxx',
            'guyslatins23',
            'latinsexnolim',
            'Thick-Kore2',
            'anahisgirl128',
            'madisonbrunette',
        ]
        dia = self.dia
        mes = self.mes
        año = self.año
        db = self.db
        if int(dia) >15:
            quincena=2
            
        if int(dia) <16:
            quincena=1   
        for modelo in modelos:
            headers = {
                'ACCESS-KEY': 'szgufgredm7vuoan5qink73qu6',
            }
            fecha= año+'-'+mes+'-'+dia
            params = (
                ('username', modelo),
                ('date_from', fecha),
                ('date_to', fecha),
            )

            response = requests.get('https://bongacams.com/api/v1/stats/model-regular-earnings', headers=headers, params=params)
            data = response.json()
            if data is not None:
                model=(data['username'])
                print(model)
                valor=(data['with_percentage_rate_income'])
                valor =float(f"{valor:.2f}")
                if valor > 0:
                    db.child('bonga').child(model).child(año+mes+str(quincena)).child(dia).set(valor)
                    GuardarEstadistica('olimpostudio1-bonga', model, dia, mes, año, valor).save()
    
    def flirt4Free(self):
        try:
            self.cargarFlirt4free1()
            self.resultado['flirt1'] = 'exitosa'
        except Exception as e:
            print(e)
            self.resultado['flirt1'] = 'fallo'
    
    def cargarFlirt4free1(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        db = self.db
        load_dotenv()
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("prefs", {
            "download.default_directory": "/var/adminstudioolimpo/backend/archivos",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        estadistica= 'https://studios.flirt4free.com/broadcasters/stats-export.php?a=studio_overview&studio=GHJQ&date_start='+año+'-'+mes+'-'+dia+'&date_end='+año+'-'+mes+'-'+dia+'&format=csv'
        browser.get(estadistica)
        user = browser.find_element('id', 'username_field')
        if user is not None:
            user.send_keys("olimpostudio")
        password = browser.find_element('id', 'password_field')
        if password is not None:
            password.send_keys("Zeus2020**")
        time.sleep(2)
        agree = browser.find_element('name', 'checkbox_agreement')
        if agree is not None:
            agree.click()
        sumbit = browser.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/div[2]/form/button')
        if sumbit is not None:
            sumbit.click()

        time.sleep(3)
        browser.close()

        if int(dia) >15:
            quincena=2
        if int(dia) <16:
            quincena=1   

        ejemplo_dir= "/var/adminstudioolimpo/backend/archivos"
        direct=[]
        directorio = pathlib.Path(ejemplo_dir)
        for fichero in directorio.iterdir():
            direct.append(fichero.name)


        filename = ejemplo_dir + "/"+direct[0]

        data = pandas.read_csv(filename)
        data1 = np.asarray(data)
        cantidad = data1.shape[0]
        remove(filename)

        for i in range (0, cantidad ) :
            db.child('flirt4free').child(str(data1[i][0])).child(año+mes+str(quincena)).child(dia).set(data1[i][21]*1.86/60)
            GuardarEstadistica('olimpostudio-flirt', str(data1[i][0]), dia, mes, año, data1[i][21]*1.86/60).save()
    
    def streamate(self):
        try:
            self.cargarStreamate1()
            self.resultado['streamate1'] = 'exitosa'
        except Exception as e:
            print(e)
            self.resultado['streamate1'] = 'fallo'

    def cargarStreamate1(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        db = self.db
        load_dotenv()
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("prefs", {
            "download.default_directory": "/var/adminstudioolimpo/backend/archivos",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        browser = webdriver.Chrome(options=options)

        browser.get('https://www.streamatemodels.com/smm/login.php')
        time.sleep(7)
        user = browser.find_element('xpath', '/html/body/div/div/div/main/div/div/div/div/form/fieldset/span[1]/div/input')
        if user is not None:
            user.send_keys("olimpowebstudio@gmail.com")
        password = browser.find_element('id', 'password')
        if password is not None:
            password.send_keys("Zeus2020**")
        browser.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        
        sumbit = browser.find_element('xpath', '/html/body/div/div/div/main/div/div/div/div/form/fieldset/button')
        if sumbit is not None:
            sumbit.click()


        print('Estadisticas Streamate')
        mesfecha=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] 

        time.sleep(3)
        estadistica= 'https://www.streamatemodels.com/smm/reports/earnings/EarningsReportPivot.php?range=day&earnday='+mesfecha[int(mes)-1]+'%20'+dia+',%20'+año+'&earnyear=2021&earnweek=1626480000&studio_filter=0&format=csv_summary'
        browser.get(estadistica)
        time.sleep(2)
        browser.quit()

        if int(dia) >15:
            quincena=2
        if int(dia) <16:
            quincena=1  
        time.sleep(2)
        ejemplo_dir= "/var/adminstudioolimpo/backend/archivos"
        direct=[]
        directorio = pathlib.Path(ejemplo_dir)
        for fichero in directorio.iterdir():
            direct.append(fichero.name)

        nombre=[]
        monto=[]
        junta=[]

        alica=ejemplo_dir + '/'+ direct[0]
        print(alica)

        filename = ejemplo_dir + "/"+direct[0]

        data = pandas.read_csv(filename, encoding='latin-1')
        data1 = np.asarray(data)
        cantidad = data1.shape[0]

        for i in range (0,cantidad):
            if data1[i][0]>0:
                nombre.append(data1[i][1])
                monto.append(data1[i][7][1:len(data1[i][7])])




        for i in range (0,len(nombre)):
            db.child('streamate').child(nombre[i]).child(año+mes+str(quincena)).child(dia).set(monto[i])
            GuardarEstadistica('olimpo-stream', nombre[i], dia, mes, año, monto[i]).save()

        remove(alica)

    def jasmin(self):
        try:
            self.cargarJasmin1()
            self.resultado['jasmin1'] = 'exitosa'
        except Exception as e:
            self.resultado['jasmin1'] = f'{e}'

    def cargarJasmin1(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        db = self.db
        if int(dia) >15:
            quincena=2
        if int(dia) <16:
            quincena=1  
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_experimental_option("prefs", {
        #     "download.default_directory": "/var/adminstudioolimpo/backend/archivos",
        #     "download.prompt_for_download": False,
        #     "download.directory_upgrade": True,
        #     "safebrowsing_for_trusted_sources_enabled": False,
        #     "safebrowsing.enabled": False
        # })
        browser = webdriver.Chrome(options=options)
        pagina = 'https://modelcenter.livejasmin.com/es/login'
        estadistica= 'https://modelcenter.livejasmin.com/es/payout/income-statistics?fromDate='+año+'-'+mes+'-'+dia+'&toDate='+año+'-'+mes+'-'+dia+'&status=all&category=all'
        browser.get(pagina)
        user = browser.find_element('id', 'emailOrNick')
        if user is not None:
            user.send_keys("olimpowebstudio@gmail.com")
        password = browser.find_element('id', 'password')
        if password is not None:
            password.send_keys("Zeus2020**")
        time.sleep(5)
        wait = WebDriverWait(browser, 10)
        # sumbit = browser.find_element(By.CSS_SELECTOR, "div > button[type='submit']")
        try:
            cookie_accept_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='cookie-consent-banner-accept']")))
            cookie_accept_button.click()
        except: pass
        sumbit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div > button[type='submit']")))
        if sumbit is not None:
            sumbit.click()
       
        time.sleep(4)
        browser.get(estadistica)
        sopa = browser.page_source

        self.scraping(sopa)
        for i in self.datos_tabla:
            if 'Modelo' in i[0]:
                continue
            if 'Income Summary' in i[0]:
                break
            modelo = i[0].replace('\n','').replace('\t','')
            cantidad = i[1].replace('$','')
            print(modelo, cantidad)
            db.child('jasmin').child((modelo)).child(año+mes+str(quincena)).child(dia).set(str(cantidad))
            GuardarEstadistica('olimpo-jasmin', modelo, dia, mes, año, cantidad).save()
    
    def imlive(self):
        try:
            self.cargarImlive1()
            self.resultado['imlive1'] = 'exitosa'
        except Exception as e:
            print(e)
            self.resultado['imlive1'] = f'{e}'
    
    def cargarImlive1(self):
        dia = self.dia
        mes = self.mes
        año = self.año
        db = self.db
        if int(dia) >15:
            quincena=2
        if int(dia) <16:
            quincena=1  
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(options=options)
        pagina = 'https://studio.imlive.com/#/'
        estadistica= 'https://studio.imlive.com/#/Studio/Statistics'
        browser.get(pagina)
        log = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/a/span')
        if log is not None:
            log.click()
        user = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[2]/input')
        if user is not None:
            user.send_keys("olimpostudioll")
        password = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[3]/input')
        if password is not None:
            password.send_keys("Zeus2020**")
        time.sleep(2)
        # wait = WebDriverWait(browser, 10)
        # sumbit = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[4]')
        # if sumbit is not None:
        #     sumbit.click()
        # time.sleep(4)
        # browser.get(estadistica)
        # time.sleep(4)
        # submit = wait.until(EC.element_to_be_clickable(('xpath', "/html/body/div/div/div[1]/div[2]/div/section/div[2]/div[2]/div/div/div[2]")))
        # if sumbit is not None:
        #     sumbit.click()
        # time.sleep(4)
        # sopa = browser.page_source

        # self.scraping(sopa)
        # data = self.datos_tabla
        # for i in data:
        #     modelo = i[1].replace('Last seen: Total Earning: $   Status: Approved. Block','')
        #     cantidad = i[9].replace('$','')
        #     if float(cantidad) > 0:
        #         diaQuincena = 15 if quincena == 1 else 30
        #         db.child('imlive').child((modelo)).child(año+mes+str(quincena)).child(diaQuincena).set(str(cantidad))
        
        browser.quit()