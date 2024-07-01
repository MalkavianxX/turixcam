from django.shortcuts import render

# Create your views here.
def init_page_evento(request):
    return render(request, 'pages/init.html')