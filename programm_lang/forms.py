from django import forms
from . import models


class ProgramLangForm(forms.ModelForm):
    class Meta:
        model = models.ProgramLang
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.ReviewProgLang
        fields = '__all__'