from rest_framework import serializers

from retail.models import Retail


class RetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Retail """

    class Meta:
        model = Retail
        exclude = ('company_date_creation',)


class RetailListSerializer(serializers.ModelSerializer):
    """ Сериализатор для вывода списка компаний """

    class Meta:
        model = Retail
        fields = '__all__'


class RetailUpdateSerializer(serializers.ModelSerializer):
    """ Сериализатор для изменения компании """

    class Meta:
        model = Retail
        exclude = ('debt_to_supplier',)
