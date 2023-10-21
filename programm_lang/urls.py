from django.urls import path
from . import views

urlpatterns = [
    path('', views.programm_lang_view),
    path('lang_detail/<int:id>/', views.programm_lang_detail_view),
    path('lang_list/', views.programm_lang_delete_view),
    path('lang_list/<int:id>/delete/', views.programm_lang_drop_view),
    path('create_post_lang/', views.createLangPostView),
    path('add-cooment/', views.createProgrammLangView),
]