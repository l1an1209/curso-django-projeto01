from django.contrib import admin
from .models import Receita

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('data_publicacao',)
    ordering = ('-data_publicacao',)
