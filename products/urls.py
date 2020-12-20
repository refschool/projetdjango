from django.urls import path
from . import views




urlpatterns = [
    path('',views.index),
    path('monform', views.monform),# path(url,view.method)
    path('get_name', views.get_name),
    path('add_product_form', views.add_product_form),
    path('editform/<str:pk>/', views.edit_product,name="edition"),#use model form
    path('thanks', views.thanks),

]


