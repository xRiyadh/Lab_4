from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="tax_app"),

    path("taxrate", views.tax_r, name="tax_app"),

    path("<int:num>", views.greet, name="greet"), 

]