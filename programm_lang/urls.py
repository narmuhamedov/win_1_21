from django.urls import path
from . import views

app_name='langs'
urlpatterns = [
    path('', views.ProgrammLangView.as_view(), name='lang_list'),
    path('lang_detail/<int:id>/', views.ProgramLangDetailView.as_view()),
    path('lang_list/<int:id>/delete/', views.ProgrammLangDropView.as_view()),
    path('lang_list/<int:id>/update/', views.UpdateLangPostView.as_view()),
    path('create_post_lang/', views.CreateLangPostView.as_view()),
    path('add-cooment/', views.createProgrammLangView),
    path('seacrh/', views.SearchView.as_view(), name='search'),
]