from rest_framework.routers import DefaultRouter
from .views import DeliveryViewSet

app_name = 'logistics'

router = DefaultRouter()
router.register(r'deliveries', DeliveryViewSet, basename='delivery')

urlpatterns = router.urls
