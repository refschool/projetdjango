from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path('new', views.new),
    path('add', views.add),
    path('monform', views.monform),# path(url,view.method)
    path('get_name', views.get_name),
    path('add_product_form', views.add_product_form),
    path('editform/<str:pk>/', views.edit_product,name="edition"),#use model form
    path('thanks', views.thanks),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)