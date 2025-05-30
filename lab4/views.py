from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextInputForm
from .igry5 import check5


# Create your views here.
def input_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            # Get the cleaned data
            a = form.cleaned_data['mat1']
            b = form.cleaned_data['mat2']

            # Redirect to the result view  
            s, m = check5(a,b) 
            res = '%s<br>%s' %(s, m)
            print('ss')
            return HttpResponse(res)
    else:
        form = TextInputForm()

    return render(request, 'input.html', {'form': form})