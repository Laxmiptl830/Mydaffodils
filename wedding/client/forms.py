from django import forms
import re

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")
    contact_number = forms.CharField(
        max_length=10,
        min_length=10,
        label="Contact Number",
        help_text="Enter exactly 10 digits"
    )

    def clean_contact_number(self):
        number = self.cleaned_data.get('contact_number')
        if not re.match(r'^\d{10}$', number):
            raise forms.ValidationError("Contact number must be exactly 10 digits.")
        return number
