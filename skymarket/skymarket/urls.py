from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# TODO здесь необходимо подклюючит нужные нам urls к проекту

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_obtain'),
    path("", include("users.urls")),
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
