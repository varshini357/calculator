from django.shortcuts import render
from .forms import CalculatorForm
from .models import *

def calculator_view(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['number1']
            n2 = form.cleaned_data['number2']
            op = form.cleaned_data['operation']

            if op == 'add':
                result = n1 + n2
                AdditionResult.objects.create(number1=n1, number2=n2, result=result)
            elif op == 'sub':
                result = n1 - n2
                SubtractionResult.objects.create(number1=n1, number2=n2, result=result)
            elif op == 'mul':
                result = n1 * n2
                MultiplicationResult.objects.create(number1=n1, number2=n2, result=result)
            elif op == 'div':
                result = n1 / n2 if n2 != 0 else 0
                DivisionResult.objects.create(number1=n1, number2=n2, result=result)

            AllOperations.objects.create(operation=op, number1=n1, number2=n2, result=result)
    else:
        form = CalculatorForm()

    return render(request, 'calculator.html', {'form': form, 'result': result})
