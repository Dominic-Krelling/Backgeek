from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from backgeek.views import CalcaViewSet, CamisetaViewSet, ChapeuViewSet, TenisViewSet

router = DefaultRouter()

router.register(r"calca", CalcaViewSet)
router.register(r"camiseta", CamisetaViewSet)
router.register(r"chapeu", ChapeuViewSet)
router.register(r"tenis", TenisViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]