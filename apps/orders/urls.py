from rest_framework.routers import DefaultRouter
from .views import CartViewSet, OrderViewSet

app_name = 'orders'

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls
