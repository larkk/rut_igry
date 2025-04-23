from django import forms

class TextInputForm(forms.Form):
    mat1 = forms.CharField(label='Первая матрица', max_length=100,  widget=forms.TextInput(attrs={'placeholder': '0 1 2 3'}))
    mat2 = forms.CharField(label='Вторая матрица', max_length=100,widget=forms.TextInput(attrs={'placeholder': '4 5 6 7'}))
    ans = forms.CharField(label='Ответ', max_length=100,widget=forms.TextInput(attrs={'placeholder': '8 51/11'}))