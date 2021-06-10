from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import Employee
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse


def index(request):
    Customer = apps.get_model('customers.Customer')
    if Customer.zip_code == Employee.zip_code:
        print(Customer.name)
    return render(request, 'employees/index.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.user
        zipcode = request.POST.get('zipcode')
        new_employee = Employee(name=name, user=user, zipcode=zipcode)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


