from django.contrib import admin
from .models import *

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    list_filter = ["nome"]
    search_fields = ["nome"]
admin.site.register(Categoria, CategoriaAdmin)
