
import os
from binance.client import Client
from time import sleep

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET")
symbol = os.getenv("SYMBOL", "BTCUSDT")
quantity = float(os.getenv("QUANTITY", "0.001"))

client = Client(api_key, api_secret)

def buy():
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    print("Alım emri gönderildi:", order)

def sell():
    order = client.order_market_sell(symbol=symbol, quantity=quantity)
    print("Satış emri gönderildi:", order)

# Basit örnek: Sadece alım yap ve çık
buy()
