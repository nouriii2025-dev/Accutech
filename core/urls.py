from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("solutions/", views.solutions, name="solutions"),
    path("products/", views.products, name="products"),
    path("projects/", views.projects, name="projects"),
    path("brands/", views.brands, name="brands"),
    path("contact/", views.contact, name="contact"),
]
