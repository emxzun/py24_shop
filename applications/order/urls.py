from django.urls import include, path
from rest_framework.routers import DefaultRouter

from applications.order.views import OrderAPIView

router = DefaultRouter()
router.register('', OrderAPIView)

urlpatterns = [
    path('', include(router.urls))
]
