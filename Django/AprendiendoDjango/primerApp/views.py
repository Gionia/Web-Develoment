from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def saludo(response):
    return render(response, "layout.html")


def index(response):
    return render(response, "index.html")


def content(response):
    return render(response, "content.html")


def contact(response):
    return render(response, "contact.html")
