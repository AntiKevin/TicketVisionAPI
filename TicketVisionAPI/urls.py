from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Core.views import ChamadosViewSet, AdminsExtraViewSet, AreasViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'Chamados', ChamadosViewSet)
router.register(r'AdminsExtra', AdminsExtraViewSet)
router.register(r'Areas', AreasViewSet)

urlpatterns = [
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('auth-token/', TokenObtainPairView.as_view()),
    path('auth-refresh-token/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
]