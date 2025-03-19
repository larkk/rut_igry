from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextInputForm
from .igry2 import *

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)



def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def input_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            a1,a2 = form.cleaned_data['mat1'],form.cleaned_data['mat2']
            a3,a4 = form.cleaned_data['mat3'],form.cleaned_data['mat4']
            a = [a1,a2,a3,a4]
            q = form.cleaned_data['q']
            mul = form.cleaned_data['mul']
            val = form.cleaned_data['val']
            sev = form.cleaned_data['sev']
            gur = form.cleaned_data['gur']
            by = form.cleaned_data['bayes']
            la = form.cleaned_data['lapl']
            hl = form.cleaned_data['hl']
            g = form.cleaned_data['g']
            gh = form.cleaned_data['gh']
            valTrue, sevTrue, gurTrue, byTrue, laTrue, hlTrue, gTrue, ghTrue =  compute(a,q,mul)
            valAnswer = 'Правильно' if abs(float(val) - valTrue) < 0.1 else 'Не верно'
            sevAnswer = 'Правильно' if abs(float(sev) - sevTrue) < 0.1 else 'Не верно'
            gurAnswer = 'Правильно' if abs(float(gur) - gurTrue) < 0.1 else 'Не верно'
            byAnswer = 'Правильно' if abs(float(by) - byTrue) < 0.1 else 'Не верно'
            laAnswer = 'Правильно' if abs(float(la) - laTrue) < 0.1 else 'Не верно'
            hlAnswer = 'Правильно' if abs(float(hl) - hlTrue) < 0.1 else 'Не верно'
            gAnswer = 'Правильно' if abs(float(g) - gTrue) < 0.1 else 'Не верно'
            ghAnswer = 'Правильно' if abs(float(gh) - ghTrue) < 0.1 else 'Не верно'
            # Redirect to the result view   
            return render(request, 'result.html', {'val': valAnswer, 'sev': sevAnswer, 'gur': gurAnswer,\
            'by': byAnswer, 'la': laAnswer, 'hl': hlAnswer, 'g':gAnswer, 'gh':ghAnswer})
    else:
        form = TextInputForm()

    return render(request, 'input.html', {'form': form})

def result_view(request):
    return render(request, 'result.html')