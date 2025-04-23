from django.http import HttpResponse

def index(request):
    s = """<a href = /lab2> Вторая лабораторная. Игры с природой </a>
    <br> 
    <a href = /lab3> Третья лабораторная. Многосторонние игры </a>
    <br> 
    <a href = /lab4> Четвертая лабораторная. Антагонистическая игра</a>
    <br> 
    <a href = /lab5> Пятая лабораторная. Диадическая игра</a>
    <br> 
    """
    return HttpResponse(s)