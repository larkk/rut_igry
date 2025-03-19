from django import forms

class TextInputForm(forms.Form):
    h = forms.CharField(label='Введите через пробел вектора выигрышей для каждой ситуации', max_length=300,  widget=forms.TextInput(attrs={
            'style': 'width: 100%;',  # Makes the input field span the full width
            'placeholder': '4 6 4 7 2 4 6 7 2 7 5..',
        }))
    u_sol = forms.CharField(label='Введите через пробел вектора из столбцов приемлемых ситуаций', max_length=300,widget=forms.TextInput(attrs={
            'style': 'width: 90%;',  # Makes the input field span the full width
            'placeholder': '1 1 1 1 1 1 1 1 -1 1 -1...',
        }))
    ravn = forms.CharField(label='Номера ситуаций равновесия в чистых стратегиях', max_length=300,widget=forms.TextInput(attrs={
            'style': 'width: 100%;',  # Makes the input field span the full width
            'placeholder': '2 4 8',
        }))
    paro = forms.CharField(label='Номера Парето-оптимальных ситуаций:', max_length=300,widget=forms.TextInput(attrs={
            'style': 'width: 100%;',  # Makes the input field span the full width
            'placeholder': '1 2 7',
        }))
    