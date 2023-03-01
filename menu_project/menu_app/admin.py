from django.contrib import admin
from .models import Menu, CategoriesMenu


@admin.register(Menu)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


@admin.register(CategoriesMenu)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'id']

