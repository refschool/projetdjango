from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('new', views.new),
    path('add', views.add),
    path('monform', views.monform),# path(url,view.method)
    path('get_name', views.get_name),
    path('product_form', views.product_form),
    path('editform/<str:pk>/', views.edit_product,name="edition"),#use model form
    path('thanks', views.thanks),
]