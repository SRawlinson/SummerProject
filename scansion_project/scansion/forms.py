from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, help_text="Enter your text here")
   
