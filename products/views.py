from django.views.generic import TemplateView, ListView, DetailView
from .models import Product


class Index(TemplateView):
    template_name = 'index.html'


class ProductsListView(ListView):
    template_name = 'list.html'
    model = Product


class ProductsDetailView(DetailView):
    template_name = 'detail.html'
    model = Product


def add_to_follow_list(request, pk):
    return True
