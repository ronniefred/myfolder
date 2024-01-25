
from django.urls import path
from .import views

app_name = 'west'
urlpatterns = [
    path("", views.world, name='home'),
    path("contact/", views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("feedback/", views.feedback, name="feedback"),
]
