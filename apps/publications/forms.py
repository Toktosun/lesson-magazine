from django import forms


class UserMailForm(forms.Form):
    """Форма для приёма данных для рассылки писем"""
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
