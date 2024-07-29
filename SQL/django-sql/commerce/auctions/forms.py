from django import forms
from .models import User, Listing, Bid, Comment



class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'bid', 'img_url', 'category']

    _categories = ["Fashion", "Toys", "Electronics", "Home", "Other"]
    category = forms.ChoiceField(choices=[(cat, cat) for cat in _categories])
    # override the default category field to use a ChoiceField with the categories list



