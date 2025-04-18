from django.shortcuts import render

# Create your views here.


def lista_posteo(request):
    return render(request,'lista_posteo.html',{})