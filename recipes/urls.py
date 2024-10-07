from django.urls import path
from recipes import views
from recipes.views import home , inicio

urlpatterns = [
    path('', home),
    path('inicio/', inicio),
    
   
]