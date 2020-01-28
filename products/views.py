from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .forms import ProductFrom
from .models import Product

# def home(request):
#     return render(request,'index.html')

class Inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')
    

def hello_world(request):
    # return HttpResponse('<h1>Hola mundo cruel</h1>')
    product = Product.objects.order_by('id')
    template = loader.get_template('products.html')
    title = 'Productos'
    context = {
        'products': product,
        'title' : title,
    }
    return HttpResponse(template.render(context, request))

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = loader.get_template('product_detail.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

def new_product(request):
    if request.method == 'POST':
        form = ProductFrom(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductFrom()


    template = loader.get_template('new_product.html')    
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))