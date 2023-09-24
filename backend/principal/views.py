from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .models import Account, Master, Earning, Period
from .serializers import CountrySerializer
import requests  #Importamos la librería requests
from datetime import date, datetime, timedelta

# Create your views here.

@api_view(["GET"])
def cargarChaturbate(request, dia, mes, año, save):
    chaturbate1 = Chaturbate('olimpostudio', 'H7tzkuPi7FXZgw8LAzuVGdwh', dia, mes, año)
    chaturbate2 = Chaturbate('olimpostudioll', 'Cl9NSMn4hqMx6zT71z0vAIWu', dia, mes, año)
    if save == 'true':
        chaturbate1.save()
        chaturbate2.save()
    return Response({'olimpostudio': chaturbate1.stats, 'olimpostudioll': chaturbate2.stats})

@api_view(["GET"])
def cargarStripchat(request, dia, mes, año, save):
    stripchat1 = Stripchat('olimpostudio-strip', '9654e575d4dfb558a0d6475f9b757b90b61548d3e3df1a069f2522b8b6d2', '4650611', '1tkzc5a6jmiv0nhy', dia, mes, año)
    stripchat2 = Stripchat('olimpostudioll-strip', 'cdac6eb583d0ec26c3fb835a30c202921b05e975b93ac230d342f5777403', '73672961', 'mf193dw8tqgvoj76', dia, mes, año)
    stripchat3 = Stripchat('juantokens-strip', '8c2b28af15673f1eb4f616c84ce7f5ff6d949d2a2ccec2fe750a733ef3d4', '108233691', '7htn1dkp4cxqv36w', dia, mes, año)
    if save == 'true':
        stripchat1.save()
        stripchat2.save()
        stripchat3.save()
    return Response({'olimpostudio':stripchat1.stats, 'olimpostudioll':stripchat2.stats, 'nacache':stripchat3.stats})

class Chaturbate:

    def __init__(self, username, token, dia, mes, año):
        self.username = username
        self.token = token
        self.dia = dia
        self.mes = mes
        self.año = año
        self.URL =f'https://chaturbate.com/affiliates/apistats/?username={self.username}&token={self.token}&stats_breakdown=sub_account__username&campaign=&search_criteria=2&period=0&language=es&date={año}-{mes}-{dia}' #configuramos la url
        self.cargarDatos()

    def cargarDatos(self):
        mensaje = ''
        stats = {}
        today = date.today()
        data = requests.get(self.URL) 
        data = data.json() #convertimos la respuesta en dict
        print(data, 'estos son')
        if data['stats'] == []: 
            stats={}
        else:
            data = data['stats'][1] if len(data['stats'])>1 else  data['stats'][0]   
            for i in range (0,len(data['rows'])):
                stats[data['rows'][i][0]] = data['rows'][i][2]
        self.stats = stats
    
    def save(self):
        for i in self.stats:
            print(self.username, i, self.stats[i])
            GuardarEstadistica(self.username, i, self.dia, self.mes, self.año, self.stats[i]).save()

class Stripchat:
    
    def __init__(self, username, sessionId, id, token, dia, mes, año) -> None:
        self.dia = dia
        self.mes = mes
        self.año = año
        fecha_actual = datetime(int(año), int(mes), int(dia))
        dia_siguiente = fecha_actual + timedelta(days=1)
        self.dia2 = f'{dia_siguiente.day}' if dia_siguiente.day > 9 else f'0{dia_siguiente.day}'
        self.mes2 = f'{dia_siguiente.month}' if dia_siguiente.month > 9 else f'0{dia_siguiente.month}'
        self.año2 = f'{dia_siguiente.year}'
        self.sessionId = sessionId
        self.id = id
        self.token = token
        self.username = username
        self.url = f'https://es.stripchat.com/api/front/users/{self.id}/earnings?from={self.año}-{self.mes}-{self.dia}T05%3A00%3A00Z&until={self.año2}-{self.mes2}-{self.dia2}T04%3A59%3A59Z&uniq={self.token}'
        self.cargarDatosStripchat()
    
    def cargarDatosStripchat(self):
        quincena = 2 if int(self.dia) >15 else 1 

        cookies = {
            'stripchat_com_firstVisit': '2023-04-16T14%3A40%3A49Z',
            'baseAmpl': '%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%221P9jHk2FjsHl_WPoF-K9SG%22%2C%22session_id%22%3A1682341128928%2C%22up%22%3A%7B%22page%22%3A%22index%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D',
            'alreadyVisited': '1',
            'amp_19a233': '1P9jHk2FjsHl_WPoF-K9SG.NDY1MDYxMQ==..1guplgqn0.1gupm4crp.0.70.70',
            'isVisitorsAgreementAccepted': '1',
            '_ga': 'GA1.2.1301892351.1681656050',
            '_gid': 'GA1.2.573934947.1682341133',
            'stripchat_com_sessionId': self.sessionId,
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

        response = requests.get(self.url, headers=headers, cookies=cookies)
        self.data = response.json()
        self.stats = {}
        for i in self.data['earnings']:
            self.stats[i['username']] = i['total']/20
    
    def save(self):
        for i in self.data['earnings']:
            GuardarEstadistica(self.username, i['username'], self.dia, self.mes, self.año, i['total']/20).save()


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