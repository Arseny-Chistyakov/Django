from django.contrib import admin

from products.models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # отображаемые объекты в таблице
    fields = ('name', 'category', 'image', 'description', ('price', 'quantity'))  # кастомизация в карточке товара
    readonly_fields = ('description',)
    search_fields = ('name',)  # поиск по выбранному столбцу
    ordering = ('-price',)  # сортировка по умолчанию по выбранному столбцу
