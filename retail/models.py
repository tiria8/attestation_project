from django.db import models

from products.models import Product

NULLABLE = {'blank': True, 'null': True}


class Retail(models.Model):
    """ Класс для модели сети по продаже электроники """

    FACTORY = 'завод'
    RETAIL = 'розница'
    TRADER = 'предприниматель'

    COMPANY_CHOICES = (
        (FACTORY, 'завод'),
        (RETAIL, 'розничная сеть'),
        (TRADER, 'индивидуальный предприниматель')
    )

    company_name = models.CharField(max_length=150, verbose_name='название')
    company_email = models.EmailField(verbose_name='почта')
    company_country = models.CharField(max_length=100, verbose_name='страна')
    company_city = models.CharField(max_length=100, verbose_name='город')
    company_street = models.CharField(max_length=100, verbose_name='улица')
    company_building = models.CharField(max_length=20, verbose_name='дом')
    company_type = models.CharField(max_length=20, choices=COMPANY_CHOICES, verbose_name='вид компании')
    company_supplier = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='поставщик')
    company_debt = models.DecimalField(max_digits=10, decimal_places=2, **NULLABLE, verbose_name='задолженность поставщику')
    created_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name='дата создания')
    company_products = models.ManyToManyField(Product, verbose_name='товары')

    def __str__(self):
        return f'{self.company_name}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ('company_name',)
