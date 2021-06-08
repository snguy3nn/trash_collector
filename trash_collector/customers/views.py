from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    try:
        logged_in_customer = Customer.objects.get(user=user)
        context = {
            'logged_in_customer': logged_in_customer
        }
    except:
        return HttpResponseRedirect(reverse('customer:create'))
    print(user)
    return render(request, 'customers/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.Post.get('user')
        pickup_day = request.POST.get('pickup_day')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        balance = request.POST.get('balance')
        one_time_pickup = request.POST.get('one_time_pickup')
        suspension_start = request.POST.get('suspension_start')
        suspension_end = request.POST.get('suspension_end')
        new_customer = Customer(name=name, user=user, pickup_day=pickup_day, address=address, zip_code=zip_code, balance=balance, one_time_pickup=one_time_pickup, suspension_start=suspension_start, suspension_end=suspension_end)
        new_customer.save()
        return HttpResponseRedirect(reverse('customer:index'))
    else:
        return render(request, 'customers/create.html')
