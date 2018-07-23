from django import forms
class Contactform(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Phone = forms.CharField()
    Message = forms.CharField(widget=forms.Textarea)