from django import forms
from .models import FeedBack

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 5, 'cols': 15}),
        }