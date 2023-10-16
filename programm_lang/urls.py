from django.urls import path
from . import views

urlpatterns = [
    path('', views.programm_lang_view),
    path('lang_detail/<int:id>/', views.programm_lang_detail_view),
    path('add-cooment/', views.createProgrammLangView),
]