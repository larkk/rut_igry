from django.http import HttpResponse

def index(request):
    s = """<a href = /lab2> Вторая лабораторная. Игры с природой </a>
    <br> 
    <a href = /lab3> Третья лабораторная. Многосторонние игры </a>
    <br> 
    <a href = /lab4> Четвертая лабораторная. Антагонистические игры</a>
    <br> 
    <a href = /lab5> Пятая лабораторная. Диадические игры</a>
    <br> 
    <a href = /lab6> Шестая лабораторная. Корпоративные игры</a>
    <br> 
    """
    return HttpResponse(s)