from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# import prebuilt refresh tokens and access tokens


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register", CreateUserView.as_view(), name='register'),
    path("api/token/", TokenObtainPairView.as_view(), name='get_token'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='refresh'),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")), # whenever the endpoint has api and the path is not the one among above paths then refer urls in api folder instead


]


