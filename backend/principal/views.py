from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .models import Account, Master, Earning, Period
from .serializers import CountrySerializer
import requests  #Importamos la librería requests
from datetime import date

# Create your views here.

@api_view(["GET"])
def cargarChaturbate(request, dia, mes, año, save):
    chaturbate1 = Chaturbate('olimpostudio', 'H7tzkuPi7FXZgw8LAzuVGdwh', dia, mes, año)
    chaturbate2 = Chaturbate('olimpostudioll', 'Cl9NSMn4hqMx6zT71z0vAIWu', dia, mes, año)
    if save == 'true':
        chaturbate1.save()
        chaturbate2.save()
    return Response({'olimpostudio': chaturbate1.stats, 'olimpostudioll': chaturbate2.stats})

class Chaturbate:

    def __init__(self, username, token, dia, mes, año):
        self.username = username
        self.token = token
        self.dia = dia
        self.mes = mes
        self.año = año
        self.URL = f'https://chaturbate.com/affiliates/apistats/?username={self.username}&token={self.token}&stats_breakdown=sub_account__username&campaign=&search_criteria=2&period=0&language=es&date={self.año}-{self.mes}-{self.dia}'
        self.cargarDatos()

    def cargarDatos(self):
        mensaje = ''
        stats = {}
        today = date.today()
        data = requests.get(self.URL) 
        data = data.json() #convertimos la respuesta en dict
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