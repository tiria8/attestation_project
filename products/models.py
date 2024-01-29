from django.db import models


class Product(models.Model):
    """ Класс для модели Product """

    name = models.CharField(max_length=150, verbose_name='наименование')
    model = models.CharField(max_length=150, verbose_name='модель')
    release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)
