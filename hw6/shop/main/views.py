from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import generate_products, Product
class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsView(ListView):
    template_name = 'main/products.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductView(DetailView):
    template_name = 'main/product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('detail',context)
        return context

def generate(request):
    return HttpResponse(generate_products())
