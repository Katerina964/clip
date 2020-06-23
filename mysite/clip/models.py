import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Hairclip(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='hairclip', verbose_name='photo',)
    characteristic = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()



    def __str__(self):
        return self.title


class Ordershop(models.Model):
    choice = models.ForeignKey(Hairclip, on_delete=models.CASCADE)
    date_order = models.DateTimeField('Дата заказа: ')
    total = models.PositiveSmallIntegerField(default=0)
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    town = models.CharField(max_length=20, verbose_name='Город')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(max_length=100, verbose_name='Почта')


    def was_published_recently(self):
        return self.date_order == timezone.now()


