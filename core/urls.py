from django.urls import path
from core.views import RegisterView, HomePageView, CreateAccountView


urlpatterns = [
    path("home", HomePageView.as_view(), name="home"),
    path("register", RegisterView, name="home"),
    path("createaccount", CreateAccountView, name="createaccount")

]