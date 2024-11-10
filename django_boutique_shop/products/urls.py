from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sale', views.sale, name = 'sale'),
    path('lawn', views.lawn, name = 'lawn'),
    path('ocassion', views.ocassion_wear, name = 'ocassion'),
    path('summer', views.summer_wear, name = 'summer'),
    path('winter', views.winter_wear, name = 'winter')
]
