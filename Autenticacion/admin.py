from django.contrib import admin
from .models import Mascota
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_creacion",)

admin.site.register(Mascota,MascotaAdmin)