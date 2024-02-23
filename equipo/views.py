from django.shortcuts import render
from .models import Personal
# Create your views here.
def miembro(request,id):
    personal = Personal.objects.get(id=id)
    context = {
        'personal':personal
    }
    return render(request,'equipo/miembro.html',context)