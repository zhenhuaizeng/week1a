from django import forms

class Cupcake(forms.Form):
    name = forms.CharField(label='Your Name\n', max_length=200)
    