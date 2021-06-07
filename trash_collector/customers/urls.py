from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='create_new_customer')
#    path('', views.index, address="index"),
#    path('new/', views.create, address='create_new_address')
]
