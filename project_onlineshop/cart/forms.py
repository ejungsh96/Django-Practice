from django import forms

# To make a form where clients can type in
# To process validation or escaping

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)