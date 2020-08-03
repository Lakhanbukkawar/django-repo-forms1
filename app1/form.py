from django import forms

class person(forms.Form):
    name=forms.CharField()
    add=forms.CharField()
    img=forms.ImageField()