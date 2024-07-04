from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.CharField(max_length=100)
    col = forms.CharField(max_length=100)
    image = forms.ImageField()

class ImageForm(forms.Form):
    image = forms.ImageField()