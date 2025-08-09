from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('about/', views.about_page, name='about_default'),
    path('about/<slug:tab_slug>/', views.about_page, name='about_tab'),
]
