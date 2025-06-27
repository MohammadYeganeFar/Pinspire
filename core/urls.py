from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.register_user, name='register_user'),
    path('auth/login/', views.login_user, name='login_user'),

    path('pins/', views.list_pins, name='list_pins'),
    path('pins/upload/', views.upload_pin, name='upload_pin'),
    path('pins/<int:pin_id>/', views.pin_detail, name='pin_detail'),
]
