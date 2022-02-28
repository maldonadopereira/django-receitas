from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicar')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicar',)
    list_per_page = 5


'''class ListandoCategorias(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    list_display_links = ('id', 'nome_categoria')
    search_fields = ('nome_categoria',)'''


admin.site.register(Receita, ListandoReceitas)
#admin.site.register(Categoria, ListandoCategorias)
