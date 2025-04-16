from django import forms

class TextInputForm(forms.Form):
    mat1 = forms.CharField(label='Первая матрица', max_length=100,  widget=forms.TextInput(attrs={'placeholder': '0 1 2 3 4 5'}))
    mat2 = forms.CharField(label='Вторая матрица', max_length=100,widget=forms.TextInput(attrs={'placeholder': '6 7 8 9 10'}))