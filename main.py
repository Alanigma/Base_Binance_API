#Importa a API da Binance
#pip install python-binance
from binance.client import Client

#Chaves para acessar sua conta da Binance
api_key = 'API KEY'
api_secret = 'API SECRET'

#Faz a conexão com a Binance
client = Client(api_key, api_secret)

#Pega as informações da sua conta da Binance como um dicionário
info = client.get_account()

print(info)
