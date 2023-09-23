from django.urls import path
from .views import ImageCreateView


urlpatterns = [
    path('upload/', ImageCreateView.as_view(), name='image-upload'),
]
