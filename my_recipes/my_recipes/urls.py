from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from recipes.views import RecipeViewSet
from users.views import RegisterViewSet

router = routers.DefaultRouter()

router.register(r'register', RegisterViewSet, basename='register')
router.register(r'recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('recipes/', include(('recipes.urls', 'recipes'), namespace='recipes')),

    path('api/', include(router.urls)),
    path('api/auth/', jwt_views.TokenObtainPairView.as_view(), name='api-auth'),
    path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='api-auth-refresh'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
