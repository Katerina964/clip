import datetime
from django.db import models
from django.utils import timezone



class Hairclip(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='hairclip', verbose_name='photo',)
    characteristic = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class Ordershop(models.Model):

    date_order = models.DateTimeField('Дата заказа: ')
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    surname = models.CharField(max_length=15, verbose_name='Фамилия')
    town = models.CharField(max_length=15, verbose_name='Город')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    email = models.EmailField(max_length=15, verbose_name='Почта')


class Positions (models.Model):

    ordershop = models.ForeignKey(Ordershop, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='hairclip', verbose_name='photo',)
    title = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()


