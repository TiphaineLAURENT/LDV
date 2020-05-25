from django.urls import path
from django.contrib.auth import views as auth_views

from shopping.views import Index, Detail, Basket


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("<int:id>", Detail.as_view(), name="detail"),
    path("basket", Basket.as_view(), name="basket"),

    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
