from celery import shared_task
from .models import Coin
from celery.schedules import crontab
import requests
from celery import app

@shared_task
def create_all_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    data = requests.get(url=url).json()
    
    for i in data:
        p, _=Coin.objects.get_or_create(name=i['name'])
        p.img = i['image']
        p.symb = i['symbol']
        p.rank = i['market_cap_rank']
        try:
            if int(p.price)>int(i['current_price']):
                p.to_up = False
            else:
                p.to_up = True
        except ValueError:
            p.to_up = False
        p.price = i['current_price']
        p.market_up = i['market_cap']
        p.maxfor24 = i['high_24h']
        p.minfor24 = i['low_24h']
        p.save()
    
    print("It works "*5)
        
  