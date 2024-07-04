from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zakazy/god/', views.year, name='year'),
    path('zakazy/mesyac/', views.month, name='month'),
    path('zakazy/nedelya/', views.day, name='day'),
    path('upload/', views.upload_image_s1, name='upload_image_s1'),
    path('upload/<int:product_id>/', views.upload_image, name='upload_image'),
]