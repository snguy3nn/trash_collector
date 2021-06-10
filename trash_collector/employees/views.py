from django.shortcuts import render
from django.apps import apps
from .models import Employee
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse
from django.shortcuts import render
from datetime import datetime as dt


def index(request):
    user = request.user
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    now = dt.now()
    today = now.strftime('%A')
    try:
        logged_in_employee = Employee.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('employees:create'))
    daily_customers = []
    for customer in customers:
        if customer.zip_code == logged_in_employee.zip_code:
            daily_customers.append(customer.name)
    context = {
        'logged_in_employee': logged_in_employee,
        'customers': daily_customers,
        }
    print(user)
    return render(request, 'employees/index.html', context)


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name=name, user=user, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')

# def daily(request):
#     user = request.user
#     logged_in_employee = Employee.objects.get(user=user)
#     Customer = apps.get_model('customers.Customer')
#     customers = Customer.objects.all()
#     now = dt.now()
#     today = now.strftime('%A')
#     customer_zip_code = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
#     customer_pickup_day = customer_zip_code.filter(pickup_day=today)
#     customer_one_time_pickup = customer_zip_code.filter(one_time_pickup=today)
#     customer_suspend = customer_zip_code.filter(suspension_start=None, suspension_end=None)
#     context = {
#         'logged_in_employee': logged_in_employee,
#         'customer': customers,
#         'customer_zip_code': customer_zip_code,
#         'customer_pickup_day': customer_pickup_day,
#         'customer_suspend': customer_suspend,
#         'customer_one_time_pickup': customer_one_time_pickup
#     }
#     return render(request, 'employees/index.html', context)