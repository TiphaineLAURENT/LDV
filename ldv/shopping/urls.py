from django.urls import path

from shopping.views import Index, Detail, Basket, Login, Logout


urlpatterns = [
    path("", Index.as_view(), name="shop"),
    path("<int:id>", Detail.as_view(), name="detail"),
    path("basket", Basket.as_view(), name="basket"),

    path("login", Login.as_view(), name="login"),
    path("logout", Logout.as_view(), name="logout"),
]
