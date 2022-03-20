from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class CasaAdmin(admin.ModelAdmin):
    list_display = ["id", "valor"]
    list_filter = ["id"]
    search_fields = ["id"]
admin.site.register(Casa, CasaAdmin)


class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ["id", "valor", "data", "investimento_total", "link"]
    list_filter = ["data"]
    search_fields = ["valor"]

    def link(self, obj):
        url = reverse('imoveis', args=(obj.pk,))
        return format_html("<a href='{}'>{}</a>", url, "Visualizar")

    link.admin_order_field = 'valor'
    link.short_description = 'Orçamento'

    def save_related(self, request, form, formsets, change):
        super(OrcamentoAdmin, self).save_related(request, form, formsets, change)
        form.instance.post_save(request)
admin.site.register(Orcamento, OrcamentoAdmin)