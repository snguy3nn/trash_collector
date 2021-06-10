from django.urls import path

from . import views


app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='create'),
    path('change/', views.change, name='change'),
    path('account/', views.account, name='account')
]
