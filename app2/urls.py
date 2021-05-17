
from django.urls import path, include
from .import views

urlpatterns = [
    path('helon', views.Testfun, name='helon'),
    path('test', views.Htmlfun, name='test'),
    path('new', views.newfun, name='new')

]
