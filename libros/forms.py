from django import forms

class ISBNForm(forms.Form):
    isbn = forms.CharField(max_length=13, label="ISBN", required=True)
