from django.shortcuts import render
from .forms import PizzaForm

def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        fild_form = PizzaForm(request.POST)
        if fild_form.is_valid():
            note = 'Your Order %s and %s pizza, is Running..' %(fild_form.cleaned_data['topping1'], fild_form.cleaned_data['topping2'] )
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', { 'pizzaForm': new_form, 'note':note })
    else:    
        form = PizzaForm()
        return render(request, 'pizza/order.html', { 'pizzaForm': form })






