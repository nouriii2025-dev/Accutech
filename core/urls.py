from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("solutions/", views.solutions, name="solutions"),
    path("products/", views.products, name="products"),
    path("products/data/", views.product_data, name="product_data"),
    path("projects/", views.projects, name="projects"),
    path("brands/", views.brands, name="brands"),
    path("terms/", views.terms, name="terms"),
    path("calibration/", views.calibration, name="calibration"),
    path("contact/", views.contact, name="contact"),
]
