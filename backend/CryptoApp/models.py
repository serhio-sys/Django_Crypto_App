from django.db import models
from django.contrib.auth import get_user_model

class Coin(models.Model):
    name = models.CharField("COIN_NAME",max_length=200)
    symb = models.CharField("COIN_SYMBOL",max_length=10)
    img = models.URLField("COIN_IMAGE")
    price = models.CharField("COIN_PRICE",max_length=200)
    rank = models.CharField("COIN_RANK",max_length=15)
    maxfor24 = models.CharField("MAX",max_length=20)
    minfor24 = models.CharField("MAX",max_length=20)
    market_up = models.CharField("COIN_M",max_length=200)
    to_up = models.BooleanField("CHECK",null=True,blank=True,default=None)
    fav = models.ManyToManyField(get_user_model(),related_name="fav",blank=True)
    