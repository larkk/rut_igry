from django import forms

class TextInputForm(forms.Form):
    task = forms.CharField(label='Введите условие', max_length=100,  widget=forms.TextInput(attrs={'placeholder': '5 8 7 19 21 25 39'}))
    z = forms.CharField(label='Минимальное значение характеристической функции максимальной коалиции, при котором ядро ещё существует', max_length=100, widget=forms.TextInput(attrs={'placeholder': '4.03'}))
    koor = forms.CharField(label='Координаты точек пересечения', max_length=100,widget=forms.TextInput(attrs={'placeholder': '(11 8 20) (5 14 20) (5 18 16) (14 18 7) (14 8 17)'}))
    weight = forms.CharField(label='Координаты центра тяжести ядра', max_length=100,widget=forms.TextInput(attrs={'placeholder': '9.8 13.2 16'}))
    shepli = forms.CharField(label='Координаты вектора Шепли', max_length=100,widget=forms.TextInput(attrs={'placeholder': '10.5 14 14.5'}))