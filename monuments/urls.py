from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'index'),
    path('monuments/', views.monuments, name='monuments'),
    path('upload/',views.upload, name= 'upload'),
    path('predict/',views.predict, name = 'predict'),
]