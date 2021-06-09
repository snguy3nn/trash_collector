from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer


def index(request):
    user = request.user
    try:
        logged_in_customer = Customer.objects.get(user=user)
        context = {
            'logged_in_customer': logged_in_customer
        }
    except:
        return HttpResponseRedirect(reverse('customers:create'))
    print(user)
    return render(request, 'customers/index.html', context)


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        pickup_day = request.POST.get('pickup_day')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        new_customer = Customer(name=name, user=user, pickup_day=pickup_day, address=address, zip_code=zip_code)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')


def change(request, customers_id):
    if request.method == 'POST':
        customers_edit = Customer.objects.get(id=customers_id)
        customers_edit.pickup_day = request.POST.get('pickup_day')
        customers_edit.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        customers_edit = Customer.objects.get(id=customers_id)
        context = {
            'customers': customers_edit
            }
        return render(request, 'customers/change.html', context)
