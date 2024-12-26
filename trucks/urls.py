from django.urls import path
from . import views


app_name = 'trucks'

urlpatterns = [
    path('list/', views.truck_list, name='list'),
    path('create/', views.truck_create, name='create'),
    path('detail/<int:pk>/', views.truck_detail, name='detail'),
    path('delete/<int:pk>/', views.truck_delete, name='delete'),
    path('update/<int:pk>/', views.truck_update, name='update'),
    path('video-list.html', views.video_list, name='video_list'),

]