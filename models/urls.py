from django.urls import path
from . import views

urlpatterns = [

    path("all_models/", views.all_models),
    path("all_models/<int:id>/", views.all_models),

]