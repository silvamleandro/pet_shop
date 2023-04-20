from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)



class ReservaForm(forms.Form):
    nome_pet = forms.CharField()
    telefone = forms.CharField()
    dia_reserva = forms.DateField()
    observacao = forms.CharField(widget=forms.Textarea)
