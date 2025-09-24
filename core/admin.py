from django.contrib import admin
from .models import Contato, PlanoSaude

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'descricao', 'data_envio')
    list_filter = ('data_envio',)
    search_fields = ('nome', 'email', 'descricao')


class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

admin.site.register(PlanoSaude, PlanoAdmin)

from .models import Vantagem

@admin.register(Vantagem)
class VantagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descricao_resumida")

    def descricao_resumida(self, obj):
        return obj.descricao[:60] + "..." if len(obj.descricao) > 60 else obj.descricao
    descricao_resumida.short_description = "Descrição"