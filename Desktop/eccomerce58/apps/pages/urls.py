from django.urls import path
from . import views

app_name = "pixel"

urlpatterns = [
    path("", views.index, name="home"),
    path("brand_detail/<slug:brand_slug>/", views.brand_detail, name="brand_detail"),
]