from django import forms

class TextInputForm(forms.Form):
    mat1 = forms.CharField(label='Первая строка матрицы', max_length=100,  widget=forms.TextInput(attrs={'placeholder': '0 1 2 3'}))
    mat2 = forms.CharField(label='Вторая строка матрицы', max_length=100,widget=forms.TextInput(attrs={'placeholder': '4 5 6 7'}))
    mat3 = forms.CharField(label='Третья строка матрицы', max_length=100,widget=forms.TextInput(attrs={'placeholder': '8 9 10 11'}))
    mat4 = forms.CharField(label='Четвертая строка матрицы', max_length=100,widget=forms.TextInput(attrs={'placeholder': '12 13 14 15'}))
    q = forms.CharField(label='q', max_length=100,widget=forms.TextInput(attrs={'placeholder': '0.5 0.2 0.3'}))
    mul = forms.CharField(label='m, u, l', max_length=100,widget=forms.TextInput(attrs={'placeholder': '0.1 0.1 0.2'}))
    val = forms.CharField(label='критерий Вальда', max_length=100,initial='0')
    sev = forms.CharField(label='критерий Севиджа', max_length=100,initial='0')
    gur = forms.CharField(label='критерий Гурвица', max_length=100,initial='0')
    bayes = forms.CharField(label='критерий Байеса', max_length=100,initial='0')
    lapl = forms.CharField(label='критерий Лапласа', max_length=100,initial='0')
    hl = forms.CharField(label='критерий Ходжеса-Лемана', max_length=100,initial='0')
    g = forms.CharField(label='критерий Гермейера', max_length=100,initial='0')
    gh = forms.CharField(label='критерий Гермейера-Гурвица', max_length=100,initial='0')
    