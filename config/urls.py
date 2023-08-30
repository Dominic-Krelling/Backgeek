from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from backgeek.views import CamisetaViewSet
from uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r"camisetas", CamisetaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)