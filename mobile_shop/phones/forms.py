from .models import PhoneReview
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = PhoneReview
        fields = ('text',)

