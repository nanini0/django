from django.urls import path
from . import views


urlpatterns=[
    path('',views.lista_posteo,name='lista_posteo'),
]