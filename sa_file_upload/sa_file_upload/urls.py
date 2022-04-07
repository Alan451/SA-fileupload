from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file_upload/',include('file_upload.urls')),   
    path('oauth2/', include('django_auth_adfs.urls')),
]
