from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.coupon_apply, name='coupon_apply'),
    path('add/', views.add_coupon, name='add_coupon'),
]
