from django.urls import path,include
from .views import *

urlpatterns = [
    path('set_language/<language>', set_language, name='set_language'),
    path('',home,name='home'),
    path('haqqimizda',about,name='about'),
    path('bloqlar',blogs,name='blogs'),
    path('bloq/<slug>',blog,name='blog'),
    path('xidmetler',services,name='services'),
    path('xidmet/<slug>',service,name='service'),
    path('portfolio',portfolios,name='portfolios'),
    path('portfolio/<slug>',portfolio,name='portfolio'),
    path('elaqe',contact,name='contact'),
    path('message',message,name='message'),
]