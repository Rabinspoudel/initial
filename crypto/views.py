from django.shortcuts import render

# Create your views here.

import requests
API = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
data= requests.get(API).json()
print(data)


def get_crypto(request):


    data = requests.get(API).json()
    ctx={
        "data":data
    }
    return render(request,'crypto_currency.html',context=ctx)