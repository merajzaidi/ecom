

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about", views.about, name="about"),
    path("tracker", views.tracker, name="tracker"),
    path("contact", views.contact, name="contact"),
    path("search", views.search, name="search"),
    path("products/<int:myid>", views.productView, name="product"),
    path("checkout", views.checkout, name="checkout"),
]

