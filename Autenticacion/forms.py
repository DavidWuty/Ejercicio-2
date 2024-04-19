from django.forms import ModelForm
from .models import Mascota


class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields =[
                'nombre',
                'especie',
                'edad',
                'genero',
        ]