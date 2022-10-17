from django.contrib import admin
from app.models import Category, Customer, Products, Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products, AdminProduct)
admin.site.register(Order)


# username = shubham, email = torkhadeshubham555@gmail.com, password = 123

