from django.urls import path
from . import views
urlpatterns = [
    path('services/',  views.servicesview),
    path('gallery/', views.galleryview),
]