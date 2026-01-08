from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 10 or len(phone) > 15:
            raise forms.ValidationError("Phone number must be 10–15 digits.")
        return phone
