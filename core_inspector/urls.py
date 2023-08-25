from django.urls import path
from . import views

# Set up the URLs
urlpatterns = [
    path('check/', views.inspect_performance, name='inspect_performance'),
]
