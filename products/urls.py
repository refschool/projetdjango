from django.urls import path
from . import views

urlpatterns = [
    path('produits',views.index),
    path('liste',views.liste),
    path('add_product_form', views.add_product_form),# path(url,view.method)
    path('editform/<str:pk>/', views.edit_product,name="edition"),#use model form
    path('thanks', views.thanks),

]


