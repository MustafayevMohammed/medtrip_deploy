from django.shortcuts import render

# Create your views here.
from django.core.checks import messages
from .models import *
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
def add_cart(request,id):
    customer = Customer.objects.get(user=request.user)
    item = get_object_or_404(Item,id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=customer,
        ordered=False
    )
    order_qs = Order.objects.filter(users=customer,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("/")
        else:
            order.items.add(order_item)
            return redirect("/")
    else:
        order = Order.objects.create(
            users=customer,
            ordered=False,
            ordered_date=timezone.now()
        )
        order.items.add(order_item)
        order.save()
        return redirect('/')
def cart(request):
    customer = Customer.objects.filter(user=request.user)
    order = Order.objects.filter(users=customer[0])
    for item in order:
        orderitem = item.items.all()
    context={
        'orderitem':orderitem
    }
    return render(request,'cart.html',context)
def remove_cart(request,id):
    customer = Customer.objects.get(user=request.user)
    item = get_object_or_404(Item,id = id)
    order_qs = Order.objects.filter(users=customer,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=customer,
                ordered=False
            )[0]
            order_item.quantity -=1
            if  order_item.quantity <1:
                order_item.delete()
            else:
                order_item.save()
                return redirect('/')
            return redirect('/')
        return redirect("/")

def product(request):
    return render(request,'product.html')

def product_details(request):
    return render(request,'product-details.html')

def payment_method(request):
    return render(request,'payment_method.html')

def order(request):
    return render(request,'order.html')

def basket(request):
    return render(request,'basket.html')