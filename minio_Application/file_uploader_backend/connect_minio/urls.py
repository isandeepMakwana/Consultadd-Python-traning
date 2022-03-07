
from django.urls import path
from .views import FileUpload
urlpatterns = [
    path('fileUpload', FileUpload.as_view()),
]
