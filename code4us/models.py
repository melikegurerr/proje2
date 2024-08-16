from django.db import models # Django'nun models modülünü içe aktarır.

# Kategori modelini tanımlayan sınıf
class Category(models.Model): 
    name = models.CharField(max_length=100)
# Category örnekleri için okunabilir bir ad döndürür. 
    def __str__(self):
        return self.name

# Kitap modelini tanımlayan sınıf
class Book(models.Model):
    kitap_adi = models.CharField(max_length=200)
    aciklama = models.TextField()
    gorsel = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, related_name='books')
 # Book örnekleri için okunabilir bir ad döndürür.   
    def __str__(self):
        return self.kitap_adi
    
