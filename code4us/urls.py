from django.urls import path
from . import views
from .views import search_book

urlpatterns= [
    path("",views.home, name="home"),
    path("home",views.home),
    path("books",views.books, name="books"),
    path('books/<int:id>/', views.bookdetails, name='bookdetails'),
    path("books",views.books, name="books"),
    path('search/', views.search_book, name='search'),  
    path("category/<int:id>/", views.category_books, name="category_books"),
]
