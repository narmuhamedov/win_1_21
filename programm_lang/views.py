from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def programm_lang_view(request):
    lang_value = models.ProgramLang.objects.all()
    return render(request, 'programm_lang.html', {'lang_key': lang_value})


def programm_lang_detail_view(request, id):
    lang_id = get_object_or_404(models.ProgramLang, id=id)
    return render(request, 'programm_lang_detail.html', {'lang_key': lang_id})


def createProgrammLangView(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Коммент успешно добавлен</h1>')

    else:
        form = forms.ReviewForm()

    return render(request, 'create_review.html', {'form': form})

