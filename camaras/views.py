from django.shortcuts import render

# Create your views here.
def view_init_page(request):
    
    return render(request, 'camaras/view_init_page.html')

def view_detail_camara(request):
    return render(request, 'camaras/view_detail.html')