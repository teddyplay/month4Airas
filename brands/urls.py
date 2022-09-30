from django.urls import path
from . import views

urlpatterns = [

    path("all_brands/", views.all_brands ),
    path("all_model/", views.all_brands ),
    # path('add_brand/<int:pk>/', views.post_new, name='post_new'),

]

