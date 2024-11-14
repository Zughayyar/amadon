from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('amadon/checkout/', views.checkout),
    path('amadon/checkout/<int:id>', views.viewCheckout)
]
