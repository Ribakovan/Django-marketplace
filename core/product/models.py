from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class City(models.Model):
    city = models.CharField(max_length=255, verbose_name='Город')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='product_images', blank=True, null=True, verbose_name='Изображение')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    is_sold = models.BooleanField(default=False, verbose_name='Продано')
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE, verbose_name='Продавец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
