from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('django.contrib.auth.urls')),
    url(r'^emoji/', include('emoji.urls')),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
