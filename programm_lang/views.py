from django.shortcuts import render, get_object_or_404
from . import models

def programm_lang_view(request):
    lang_value = models.ProgramLang.objects.all()
    return render(request, 'programm_lang.html', {'lang_key': lang_value})


def programm_lang_detail_view(request, id):
    lang_id = get_object_or_404(models.ProgramLang, id=id)
    return render(request, 'programm_lang_detail.html', {'lang_key': lang_id})
