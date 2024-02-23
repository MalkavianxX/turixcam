from django.shortcuts import render

# Create your views here.
def miembro(request,id):
    return render(request,'equipo/miembro.html')