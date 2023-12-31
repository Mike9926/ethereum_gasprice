# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('gas-price/<int:id>/', views.gas_price_detail, name='gas_price_detail'),
    path('fetch_gas_prices/', views.fetch_gas_prices, name='fetch_gas_prices'),
    path('update-gas-price/', views.update_gas_price, name='update-gas-price'),

]