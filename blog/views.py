from django.shortcuts import render
from.models import Posteo
from django.utils import timezone
# Create your views here.


def lista_posteo(request):
    posts = Posteo.objects.filter(fecha_creacion__lt=timezone.now()).order_by('fecha_creacion')
    return render(request, 'lista_posteo.html', {'posts': posts})