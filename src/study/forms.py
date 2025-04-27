from django import forms
from taggit.forms import TagWidget

class BlogForm(forms.Form):
    title   = forms.CharField(max_length=200, label="Name of your blog")
    content = forms.CharField(widget=forms.Textarea)
    source  = forms.URLField(
                label="Source link",
                required=False,
                max_length=200,
                widget=forms.URLInput(attrs={
                    'placeholder': 'Enter a valid URL',
                    'class': 'form-control',
                }))
    tags    = forms.CharField(max_length=150, required=True, widget=TagWidget)