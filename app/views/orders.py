
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Order, Category, Product
from app.forms import OrderForm

def index(request):
    assert isinstance(request, HttpRequest)
    orders = Order.objects.all()
    return render(
        request,
        'app/orders/index.html',
        {
            'orders': orders
        }
    )

def create(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    form = OrderForm()
    return render(
        request,
        'app/orders/create.html',
        {
            'form': form,
            'categories': categories
        }
    )
    
def getProducts(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id = category_id).order_by('product_name')
    return render(
        request,
        'app/orders/getProducts.html',
        {
            'products': products
        }
    )
    
def getUnitPrice(request):
    id_product = request.GET.get('id_product')
    product = Product.objects.get(pk=id_product)
    return render(
        request,
        'app/orders/getUnitPrice.html',
        {
            'product': product
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Order has been saved successfully !")
        return redirect('/orders')