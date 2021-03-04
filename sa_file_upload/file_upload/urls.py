from django.urls import path
from . import views

urlpatterns = [
    path('file_upload/',views.file_upload,name="file_upload"),
    path('roll/',views.roll,name="roll"),
]
