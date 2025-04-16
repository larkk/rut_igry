from django.http import HttpResponse

def index(request):
    s = """<a href = /lab2> Вторая лабораторная. Игры с природой </a>
    <br> 
    <a href = /lab3> Третья лабораторная. Многосторонние игры </a>
    <br> 
    <a href = /lab5> Пятая лабораторная</a>
    <br> 
    """
    return HttpResponse(s)