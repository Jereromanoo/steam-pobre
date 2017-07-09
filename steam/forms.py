from django import forms

from .models import Juego

class JuegoForm(forms.ModelForm):
	class Meta:
		model = Juego
		fields = ('nombre','genero','descripcion','distribuidor','precio','imagen')
