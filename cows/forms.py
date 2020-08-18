from django import forms


class InputForm(forms.Form):
    phrase = forms.CharField(widget=forms.TextInput)

