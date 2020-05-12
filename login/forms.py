from django import forms


class CreatePost(forms.Form):
    title = forms.CharField(max_length=125)
    text = forms.CharField(max_length=10000)
