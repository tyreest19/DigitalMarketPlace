from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from DigitalMarketPlace.mixins import LoginRequiredMixin
from .forms import ProductAddForms
from .forms import ProductModelForm
from .models import Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'form.html'
    form_class = ProductModelForm
    success_url = '/add'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(ProductCreateView, self).form_valid(form)

class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product
    # template_name = 'list_view.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     context['queryset'] = self.get_queryset()
    #     return context

    def get_queryset(self, *args, **kwargs):
        queryset = super(ProductListView, self).get_queryset(**kwargs)
        # queryset = queryset.filter(title__icontains='Product')
        print('i am queryset', queryset)
        return queryset

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'form.html'
    form_class = ProductModelForm
    success_url = '/list'

    def get_object(self,args, **kwargs):
        user = self.request.user
        obj = super(ProductUpdateView, self).get_object(*args, **kwargs)
        if obj.user == user:
            return obj
        else:
            raise Http404


# Create your views here.
def update_view(request, id):
    #if request.user.is_authenticated:
    product = get_object_or_404(Product, id=id)
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()
    print(request.user)
    template = 'form.html'
    context = {
            'form': form,
            'submit_btn': 'Update View',
        }
    return render(request, template, context)

def create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()
    # form = ProductAddForms(request.POST or None)
    # if form.is_valid():
    #     data = form.cleaned_data
    #     title = data.get('title')
    #     description = data.get('description')
    #     price = data.get('price')
    #     new_obj = Product()
    #     new_obj.title = title
    #     new_obj.description = description
    #     new_obj.price = price
    #     new_obj.save()
    template = 'form.html'
    context = {
        'form': form,
        'submit_btn': 'Create View',
    }
    return render(request, template, context)
def detail_slug_view(request, slug):
    #if request.user.is_authenticated:
    print(slug)
    product = get_object_or_404(Product, slug=slug)
    print(request.user)
    template = 'detail_view.html'
    context = {
            'object':  product
        }
    return render(request, template, context)

def detail_view(request, id):
    #if request.user.is_authenticated:
    product = get_object_or_404(Product, id=id)
    print(request.user)
    template = 'detail_view.html'
    context = {
            'title': 'Hello detail',
            'object':  product
        }
    return render(request, template, context)


def list_view(request):
    print(request)
    queryset = Product.objects.all()
    template = 'list_view.html'
    context = {
        'queryset': queryset
    }
    return render(request, template, context)
