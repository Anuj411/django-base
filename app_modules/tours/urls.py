from django.urls import path, include
from rest_framework import routers
from .views import TourPackageView

router = routers.DefaultRouter()
router.register("tour-package", TourPackageView)

urlpatterns = [
    path("", include(router.urls)),
]
