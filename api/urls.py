from django.urls import path
from . import views

urlpatterns = [
    path("text/<str:text>/", views.convertTextToSpeech, name="convert")
]
