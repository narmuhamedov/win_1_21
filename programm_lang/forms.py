from django import forms
from . import models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.ReviewProgLang
        fields = '__all__'