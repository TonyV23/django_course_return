from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Customer
from app.forms import CustomerForm
from django.contrib import messages

def index(request):
    assert isinstance(request, HttpRequest)
    customers = Customer.objects.all()
    return render(
        request,
        'app/customers/index.html',
        {
            'customers': customers
        }
    )

def create(request):
    form = CustomerForm()
    return render(
        request, 
        'app/customers/create.html',
        {
            'form': form
        }
    )

def store(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer successfully saved")
        return redirect('/customers')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
            product = Customer.objects.get(pk=id)
            form = CustomerForm(instance=product)
        return render(
            request,
            'app/customers/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            product = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer successfully modified")
        return redirect('/customers')

def delete(request, id):
    product = Customer.objects.get(pk=id)
    product.delete()
    messages.success(request, "Customer successfully deleted")
    return redirect('/customers')
  

