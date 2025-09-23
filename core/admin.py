from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'resumo_descricao', 'data_envio')
    list_filter = ('data_envio',)
    search_fields = ('nome', 'email', 'descricao')
