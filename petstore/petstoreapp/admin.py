from django.contrib import admin
from petstoreapp.models import petstoreapp_db

# Register your models here.

class productName(admin.ModelAdmin):
    list_display = ["id","name","price","details","category"]

admin.site.register(petstoreapp_db,productName)