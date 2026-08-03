from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "company", "email", "phone", "enquiry_type", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Your name"}),
            "company": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Company (optional)"}),
            "email": forms.EmailInput(attrs={
                "class": "form-control", "placeholder": "you@company.com"}),
            "phone": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "+971 ..."}),
            "enquiry_type": forms.Select(attrs={"class": "form-select"}),
            "message": forms.Textarea(attrs={
                "class": "form-control", "rows": 5,
                "placeholder": "Tell us what you need calibrated, measured, or supplied."}),
        }
