from django.shortcuts import render

from django.shortcuts import render

from django.http import  HttpResponse
from django.shortcuts import render
import random
from datetime import datetime
from blog.models import Post
def index(request):
    {
    }
    return render(request, template_name="index.html",context={})

def home(request):
    object_list = Post.objects.all()
    ctx={
        "obj":object_list
    }
    return render(request,"home.html",context=ctx)

def about(request):
    {

    }
    return render(request,template_name="about.html",content_type={})

def contact(request):
    {
    }
    return render(request,template_name="contact.html",content_type={})
