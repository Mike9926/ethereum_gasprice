# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path("home/", views.home, name="home"),
    # About page
    path("about/", views.about, name="about"),
    # Contact page
    path("contact/", views.contact, name="contact"),
    # Gas price detail page
    path("<int:pk>/detail", views.gas_price_detail, name="gas_price_detail"),
    path('fetch_gas_prices/', views.fetch_gas_prices, name='fetch_gas_prices'),
]
