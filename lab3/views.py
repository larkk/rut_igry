from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextInputForm
from .igry3 import compute


def input_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            h = form.cleaned_data['h']
            u_sol = form.cleaned_data['u_sol']
            ravn = form.cleaned_data['ravn']
            paro = form.cleaned_data['paro']
            isRight, checkParo, checkRavn, ansFormatted =  compute(h, u_sol, ravn, paro)
            valAnswer = 'Верно' if isRight else 'Не верно'
            valAnswerParo = 'Верно' if checkParo else 'Не верно'
            valAnswerRavn = 'Верно' if checkRavn else 'Не верно'

            # Redirect to the result view   
            return render(request, 'result3.html', {'ansFormatted': ansFormatted,'valAnswer': valAnswer,\
            'valAnswerParo': valAnswerParo,'valAnswerRavn': valAnswerRavn })
    else:
        form = TextInputForm()

    return render(request, 'input.html', {'form': form})
