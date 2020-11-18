from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('new', views.new),
    path('add', views.add),
    path('monform', views.monform),
    path('get_name', views.get_name),
    path('product_form', views.product_form),
    path('thanks', views.thanks),
]