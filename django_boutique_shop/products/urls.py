from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sale', views.sale, name = 'sale'),
    path('lawn', views.lawn, name = 'lawn')
]
