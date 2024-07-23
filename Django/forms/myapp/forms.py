from django import forms
from .models import Snippet


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)  # this is a multi-line text field


class SnippetForm(forms.ModelForm):

    class Meta:  # here we specify the model and the fields we want to include in the form
        model = Snippet  # we use the snippet model
        fields = ('name', 'body')