from django.urls import path
from shopping.views import Index, Detail

urlpatterns = [
    path("", Index.as_view()),
    path("<int:id>", Detail.as_view()),
]
