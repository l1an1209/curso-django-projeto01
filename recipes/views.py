from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html',context={
        'name':'Luan'
    })

def inicio(requests):
    return render(requests,'recipes/partials/header.html')




