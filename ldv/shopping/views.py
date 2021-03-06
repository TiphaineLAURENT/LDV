from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.contrib.auth import views as auth_views

import copy

from shopping.models import Vetement, Item, User
from shopping.forms import LoginForm


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

    def post(self, request, *args, **kwargs):
        items = copy.copy(request.POST)
        items.pop('csrfmiddlewaretoken', None)
        Item.objects.filter(id__in=items.keys()).delete()
        return redirect('basket')


class Login(auth_views.LoginView):
    """
     Redirect user if already authenticated
    """

    redirect_authenticated_user = True
    extra_context = {'form': LoginForm()}


class Logout(auth_views.LogoutView):
    """
     Do nothing more that LogoutView
    """
