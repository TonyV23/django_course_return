from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Product
from app.forms import ProductForm
from django.contrib import messages


def index(request):
    assert isinstance(request, HttpRequest)
    products = Product.objects.all()
    return render(
        request,
        'app/products/index.html',
        {
            'products': products
        }
    )

def create(request):
    form = ProductForm()
    return render(
        request, 
        'app/products/create.html',
        {
            'form': form
        }
    )

def store(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully saved")
        return redirect('/products')


def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(
            request,
            'app/products/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Category successfully modified")
        return redirect('/products')

def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request, "Category successfully deleted")
    return redirect('/products')
  
    