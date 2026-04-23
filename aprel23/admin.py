from django.contrib import admin
from aprel23.models import Category, Product
# Register your models here.


@admin.register(Category)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")



@admin.register(Product)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("category", "title", "is_active")