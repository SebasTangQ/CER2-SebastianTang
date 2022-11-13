from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Residencia)
class RequestResidencia(admin.ModelAdmin):
    model = Residencia
    list_display = ['id','get_residencia','get_propietario','get_fono']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('id', 'calle', 'numero', 'fono', 'propietario')
        return self.readonly_fields

    def get_residencia(self, obj):
        return obj.calle.upper() + ' N°'+obj.numero.upper()
    get_residencia.short_description = "residencia"
    def get_propietario(self,obj):
        return obj.propietario.upper()
    get_propietario.short_description = "propietario"
    def get_fono(self,obj):
        return obj.fono.upper()
    get_fono.short_description = "fono"

@admin.register(Correspondencia)
class RequestCorrespondencia(admin.ModelAdmin):
    model = Correspondencia
    list_display = ['id','get_residencia']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('id', 'residencia', 'tipo', 'fecha_recepcion')
        return self.readonly_fields

    def get_residencia(self, obj):
        return obj.residencia.calle.upper() + ' N°'+obj.residencia.numero.upper()
    get_residencia.short_description = "residencia"
