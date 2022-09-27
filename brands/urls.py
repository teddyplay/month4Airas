from django.urls import path
from . import views

urlpatterns = [

    path("all_brands/", views.all_brands )


]

