# Generated by Django 5.0.1 on 2024-01-29 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150, verbose_name='название')),
                ('company_email', models.EmailField(max_length=254, verbose_name='почта')),
                ('company_country', models.CharField(max_length=100, verbose_name='страна')),
                ('company_city', models.CharField(max_length=100, verbose_name='город')),
                ('company_street', models.CharField(max_length=100, verbose_name='улица')),
                ('company_building', models.CharField(max_length=20, verbose_name='дом')),
                ('company_type', models.CharField(choices=[('завод', 'завод'), ('розница', 'розничная сеть'), ('предприниматель', 'индивидуальный предприниматель')], max_length=20, verbose_name='вид компании')),
                ('company_debt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='задолженность поставщику')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('company_supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retail.retail', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ('company_name',),
            },
        ),
    ]
