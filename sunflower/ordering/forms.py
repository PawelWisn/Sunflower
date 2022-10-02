from ordering.models import Order
from django import forms
from django.forms import Textarea, EmailInput
from django.utils.translation import gettext_lazy as _

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("email", "notes", "picture")
        widgets={
            "email": EmailInput(attrs={"placeholder":_("johnsmith@example.com")}),
            "notes": Textarea(attrs={"placeholder":_("Please, tell me about your sticker")}),
        }