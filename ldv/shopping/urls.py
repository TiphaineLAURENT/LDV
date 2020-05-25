from django.urls import path
from shopping.views import Index

urlpatterns = [
    path("", Index.as_view()),
]
