from django.shortcuts import render, redirect
from .models import Company, PrintProduct, Order
from .forms import OrderForm
# Create your views here.
def index(request):
    return render(request, 'corp_print_app/index.html')

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_detail(request, company_id):
    company = Company.objects.get(id=company_id)
    return render(request, 'company_detail.html', {'company': company})

def product_list(request):
    products = PrintProduct.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = PrintProduct.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_create(request, product_id):
    product = PrintProduct.objects.get(id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.total_price = product.price * order.quantity
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'product': product, 'form': form})

def order_success(request):
    return render(request, 'order_success.html')
