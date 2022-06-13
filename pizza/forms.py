from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.PasswordInput)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     #toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'),('ham', 'Ham'),('cheese', 'Cheese'),('olives', 'Olives')], widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])


class PizzaForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2', 'size': 'Size'}
        # widgets = {'size': forms.CheckboxSelectMultiple}





