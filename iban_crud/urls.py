from django.urls import path

from . import views

urlpatterns = [
    path('get_users', views.get_users, name='get_users'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('create_user', views.create_or_update_user, name='create_user'),
    path('modify_user/<int:user_id>/', views.create_or_update_user, name='modify_user'),
]