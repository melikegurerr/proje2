from django.urls import path
from . import views # views modülünü içe aktararak view fonksiyonlarını kullanıyoruz
from .views import search_book # search kısmını kullanabilmek için views fonksiyonlarını kullanıyoruz.

urlpatterns= [
    path("",views.home, name="home"), # Ana sayfanın URL'i. Eğer kullanıcı siteye doğrudan ana alan adıyla erişirse, 'home' view fonksiyonuna yönlendirilir.
    path("home",views.home),# Alternatif bir ana sayfa URL'i. Kullanıcı 'home' yazarsa, yine 'home' view fonksiyonuna yönlendirilir. 
    path("books",views.books, name="books"),# Tüm kitapların listelendiği sayfa. 'books' view fonksiyonuna yönlendirilir. Bu URL 'books' ismiyle anılabilir.
    path('books/<int:id>/', views.bookdetails, name='bookdetails'),# Belirli bir kitabın detay sayfası. URL'de kitabın ID'si dinamik olarak belirlenir. Bu, 'bookdetails' view fonksiyonuna yönlendirir ve 'bookdetails' adıyla anılabilir.
    path("books",views.books, name="books"),
    path('search/', views.search_book, name='search'), # Kitap arama sayfası. 'search_book' view fonksiyonuna yönlendirilir ve 'search' adıyla anılabilir.
    path("category/<int:id>/", views.category_books, name="category_books"),# Belirli bir kategorideki kitapları listeleyen sayfa. URL'de kategori ID'si dinamik olarak belirlenir. 'category_books' view fonksiyonuna yönlendirir ve 'category_books' adıyla anılabilir.
]