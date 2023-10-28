from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class ProgrammLangView(generic.ListView):
    template_name = 'programm_lang.html'
    queryset = models.ProgramLang.objects.all()

    def get_queryset(self):
        return models.ProgramLang.objects.all()

class ProgramLangDetailView(generic.DetailView):
    template_name = 'programm_lang_detail.html'

    def get_object(self, **kwargs):
       lang = self.kwargs.get('id')
       return get_object_or_404(models.ProgramLang, id=lang)

class CreateLangPostView(generic.CreateView):
    template_name = 'create_lang.html'
    form_class = forms.ProgramLangForm
    queryset = models.ProgramLang.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateLangPostView, self).form_valid(form=form)

class UpdateLangPostView(generic.UpdateView):
    template_name = 'update_lang.html'
    form_class = forms.ProgramLangForm
    success_url = '/'

    def get_object(self, **kwargs):
        lang = self.kwargs.get('id')
        return get_object_or_404(models.ProgramLang, id=lang)

    def form_valid(self, form):
        return super(UpdateLangPostView, self).form_valid(form=form)

class ProgrammLangDropView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        lang_id = self.kwargs.get('id')
        return get_object_or_404(models.ProgramLang, id=lang_id)

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

class SearchView(generic.ListView):
    template_name = 'programm_lang.html'
    context_object_name = 'lang'
    paginate_by = 5

    def get_queryset(self):
        return models.ProgramLang.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return contextф
