from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('images/', views.get_images, name='images'),
    path('upload/', views.post_image, name='image-upload'),
]
