from django.urls import path
from core.views import MyView, HomePageView


urlpatterns = [
    path("home", HomePageView.as_view(), name="home")
]