from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from db.models import User, Customer, Order, Product, OrderItem

admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)

