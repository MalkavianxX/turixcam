from .views import maintenance_view
class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica si el sitio está en modo de mantenimiento
    
        return maintenance_view(request)
