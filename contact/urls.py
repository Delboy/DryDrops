from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_contact_page, name='contact'),
]
