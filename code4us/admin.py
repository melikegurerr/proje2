from django.contrib import admin # Django'nun admin paneli modülünü içe aktarır
from . models import Category, Book # 'Category' ve 'Book' modellerini içe aktarır



admin.site.register(Category) # 'Category' modelini admin paneline kaydeder. Bu, admin panelinde 'Category' modelinin görünüp düzenlenmesini sağlar.
admin.site.register(Book) # 'Book' modelini admin paneline kaydeder. Bu, admin panelinde 'Book' modelinin görünüp düzenlenmesini sağlar.