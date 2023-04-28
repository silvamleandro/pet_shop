from django import forms
from base.models import Contato, Reserva

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']



class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nome_pet', 'telefone', 'dia_reserva', 'observacao']
