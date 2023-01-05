import email
from email import message
from importlib.abc import Loader
from importlib.util import LazyLoader
from json import load
from time import timezone
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from form.forms import ContactForm
import mariadb
from django.apps import apps

from form.models import contactFormModel

# Create your views here.

def index(request):

    context = dict()
    url = request.META.get('HTTP_REFERER')
    mydata = contactFormModel.objects.all()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        mydata = contactFormModel.objects.all()
        
        if contact_form.is_valid():
            message = contact_form.save(commit=False)
            message.save()
            return HttpResponseRedirect(url)

        else:
            context['form'] = ContactForm()

    return render(request, 'index.html', {"mydatas":mydata})

    
def deneme(request):
    mydata = contactFormModel.objects.all()

    return render(request, 'index.html', {"mydatas":mydata})

def connection():
    conn = mariadb.connect(
        user="myroot", #Your login user
        password="yusuf", #Your login password
        host="localhost", #Your server name 
        port=3307,
        database="form.com")
    return conn

def formlist(request):
    forms = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM form_contactformmodel")
    for row in cursor.fetchall():
        forms.append({"id": row[0], "username": row[1], "email": row[2], "message": row[3], "rating1": row[4], "rating2": row[5]})
    conn.close()
    return render(request, 'index.html', {'forms':forms})


def addform(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'form':{}})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            rating1 = form.cleaned_data.get("rating1")
            rating2 = form.cleaned_data.get("rating2")
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO TblCars (id, username, email, message, rating1, rating2) VALUES (?, ?, ?, ?, ?, ?)", (id, username, email, message, rating1, rating2) )
            conn.commit()
            conn.close()
        return HttpResponseRedirect('formlist')