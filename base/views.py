from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm

def inicio(request):
    return render(request, 'inicio.html')



def contato(request):
    contexto = {'sucesso': False}
    form = ContatoForm(request.POST or None)

    if form.is_valid():
        contexto['sucesso'] = True
        form.save()

    contexto['form'] = form
    contexto['telefone'] = '(99) 99999-9999'
    contexto['responsavel'] = 'Maria da Silva Pereira'

    return render(request, 'contato.html', contexto)



def reserva(request):
    contexto = {'sucesso': False}
    form = ReservaForm(request.POST or None)

    if form.is_valid():
        contexto['sucesso'] = True
        form.save()
    
    contexto['form'] = form

    return render(request, 'reserva.html', contexto)
