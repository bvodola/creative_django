from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^services/', views.services, name='services'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^', views.home, name='home'),
]
