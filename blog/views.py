from django.shortcuts import render

from django.shortcuts import render

from django.http import  HttpResponse
from django.shortcuts import render
import random
from datetime import datetime

def index(request):
    aa=datetime.now()
    ctx = {
        'date': aa,
        'value':"hey"
    }
    return render(request, template_name="index.html",context=ctx)

def home(request):
    r={
        'dat':[1,2,3,4,5,6,7,8,9,10]

    }
    return render(request,template_name="home.html",context=r)

def about(request):
    {
    "sdasdasdasdasddas"
    }
    return render(request,template_name="about.html",content_type={})

def contact(request):
    {
    "sdasdasdasdasddas contact us "
    }
    return render(request,template_name="contact.html",content_type={})
