from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ["name", "phone", "email", "message", "financing"]
