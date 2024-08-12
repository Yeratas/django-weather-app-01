from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<str:city>',views.delete_record,name = 'delete'),
]