from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for the contact model.
    """
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "email": forms.EmailInput(attrs={"autocomplete": "email"}),
            "name": forms.TextInput(attrs={"autocomplete": "name"}),
        }
