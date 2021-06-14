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
        'customers_address': customer.address
        }
    print(daily_customers)
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

