from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from backgeek.views import CamisetaViewSet, EstampaViewSet, MoletomViewSet
from uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r"camisetas", CamisetaViewSet)
router.register(r"estampas", EstampaViewSet)
router.register(r"moletons", MoletomViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)), 
    path("api/media/", include(uploader_router.urls)),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)