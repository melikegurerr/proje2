# Generated by Django 5.1 on 2024-08-14 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code4us', '0004_book_kategoriler'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='kategoriler',
            new_name='category',
        ),
    ]
