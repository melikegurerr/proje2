from django.urls import path
from . import views

urlpatterns= [
    path("",views.home, name="home"),
    path("home",views.home),
    path("books",views.books, name="books"),
    path("books/<int:id>",views.booksdetails, name="bookdetails"),
    path("books",views.books, name="books"),

]