from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.products.views import home_view

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root_view(request):
    data = {
        "name": "Impulso Shop API - E-commerce D2C",
        "version": "v1.0.0",
        "status": "operational",
        "public_endpoints": {
            "products": "/api/v1/products/",
            "categories": "/api/v1/products/categories/",
        },
        "protected_endpoints": {
            "cart": "/api/v1/orders/cart/",
            "orders": "/api/v1/orders/orders/",
            "logistics": "/api/v1/logistics/deliveries/",
            "profile": "/api/v1/users/me/",
        },
        "authentication_info": {
            "type": "JWT / Session",
            "login_url": "/api/v1/users/login/",
        },
    }
    return Response(data)

urlpatterns = [
    path('', home_view, name='home'),
    path('api/v1/', api_root_view, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.users.urls', namespace='users')),
    path('api/v1/products/', include('apps.products.urls', namespace='products')),
    path('api/v1/orders/', include('apps.orders.urls', namespace='orders')),
    path('api/v1/logistics/', include('apps.logistics.urls', namespace='logistics')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
