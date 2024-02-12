from django.contrib import admin
from base import models

# Register your models here.
admin.site.register(models.Cliente)
admin.site.register(models.RegistrarLocacao)


# admin.site.register(models.Immobile)
# admin.site.register(models.ImmobileImage)


class ImmobileImageInlineAdmin(admin.TabularInline):
    model = models.ImovelImagens
    extra = 0


class ImmobileAdmin(admin.ModelAdmin):
    inlines = [ImmobileImageInlineAdmin]


admin.site.register(models.Imovel, ImmobileAdmin)