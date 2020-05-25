from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from shopping.models import Vetement, Item, User

# Create your views here.

class Index(LoginRequiredMixin, TemplateView):
    """
     Index view
    """

    template_name = "shopping/shop.html"

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
        Item.objects.create(user=request.user, vetement=vetement)
        return render(request, self.template_name, {'vetement': vetement})


class Basket(LoginRequiredMixin, TemplateView):
    """
     Display basket items for a specific user
    """

    template_name = "shopping/basket.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                        {'items': request.user.items.all()})
