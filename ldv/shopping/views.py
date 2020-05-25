from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from shopping.models import Vetement, Item, User

# Create your views here.

class Index(LoginRequiredMixin, TemplateView):
    """
     Index view
    """

    template_name = "shopping/index.html"

    def get(self, request, *args, **kwargs):
        vetements = Vetement.objects.all()
        return render(request, self.template_name, {'vetements': vetements})


class Detail(LoginRequiredMixin, TemplateView):
    """
     Display one vetement
    """

    template_name = "shopping/detail.html"

    def get(self, request, id, *args, **kwargs):
        vetement = get_object_or_404(Vetement, id=id)
        user = request.user
        user.items.add(vetement)
        user.save()
        return render(request, self.template_name, {'vetement': vetement})


class Basket(LoginRequiredMixin, TemplateView):
    """
    """
