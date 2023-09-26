from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('images/', views.get_images, name='images'),
    path('images/<str:username>/', views.get_user_images, name='user-images'),
    path('upload/', views.post_image, name='image-upload'),
    path('expire-links/<str:expire_link_token>/', views.get_expire_link, name='expire-link-detail'),
]
