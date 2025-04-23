from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextInputForm
from .igry6 import check

# Create your views here.
def input_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            task = form.cleaned_data['task']
            z = form.cleaned_data['z']
            koor = form.cleaned_data['koor']
            weight = form.cleaned_data['weight']
            shepli = form.cleaned_data['shepli']
            answers = check(task, z, koor, weight, shepli)
            # Redirect to the result view  
            return render(request, 'result6.html', answers)
    else:
        form = TextInputForm()

    return render(request, 'input.html', {'form': form})