from django.urls import path
from django.contrib.auth import views as auth_views

from shopping.views import Index, Detail


urlpatterns = [
    path("", Index.as_view()),
    path("<int:id>", Detail.as_view()),
    path("login", auth_views.LoginView.as_view(), name="login"),
]
