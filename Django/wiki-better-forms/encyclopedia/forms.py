from django import forms
from .util import get_entry


class CreateEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

    def clean_title(self):
        title = self.cleaned_data["title"]
        if get_entry(title) is not None:
            raise forms.ValidationError("The entry already exists")
        return title
