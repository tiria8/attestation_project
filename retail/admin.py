from django.contrib import admin

from django.utils.html import format_html

from retail.models import Retail


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_city', 'company_type', 'supplier_url', 'company_debt')
    list_filter = ('company_city',)
    actions = ['remove_debt']

    def remove_debt(self, request, queryset):
        for item in queryset:
            item.company_debt = 0
            item.save()
        self.message_user(request, 'Задолженность перед поставщиком обнулена.')

    remove_debt.short_description = 'Обнулить задолженность'

    def supplier_url(self, obj):
        """ Получение ссылки на поставщика """

        supplier = obj.company_supplier
        try:
            supplier_id = supplier.id
            url = f'{supplier_id}/change/'
            return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.company_supplier)
        except AttributeError:
            pass

    supplier_url.short_description = 'Поставщик'
