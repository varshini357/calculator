from django import forms

class CalculatorForm(forms.Form):
    number1 = forms.FloatField()
    number2 = forms.FloatField()
    operation = forms.ChoiceField(choices=[
        ('add', 'Add'),
        ('sub', 'Subtract'),
        ('mul', 'Multiply'),
        ('div', 'Divide')
    ])
