from django.shortcuts import render
from .models import Category, Book

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "kitaplar" : Book.objects.filter(anasayfa=True),
    }
    return render(request, "index.html", data)

def books(request):
    data = {
        "kategoriler": Category.objects.all(),
        "kitaplar" : Book.objects.all(),
    }
    return render(request, "books.html", data)

def booksdetails(request,id):
    data = {
        "book": Book.objects.get(id=id)
    }
    return render(request, "details.html", data)