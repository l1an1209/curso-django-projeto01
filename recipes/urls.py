from django.urls import path
from recipes import views
from recipes.views import home 

urlpatterns = [
    path('', home),
    path('lista-receitas/', views.lista_receitas, name='lista_receitas'),  
]