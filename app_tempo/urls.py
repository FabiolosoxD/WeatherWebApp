from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('limpar/', views.limpar_cidades, name='limpar_cidades'),
]
