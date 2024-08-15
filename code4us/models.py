from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    kitap_adi = models.CharField(max_length=200)
    aciklama = models.TextField()
    gorsel = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, related_name='books')
    
    def __str__(self):
        return self.kitap_adi
    
