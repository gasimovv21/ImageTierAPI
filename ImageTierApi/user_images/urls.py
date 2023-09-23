from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('upload/', views.post_images, name='image-upload'),
]
