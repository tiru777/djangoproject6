from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.forms import EmployeeForm
from app.models import Employee


def home(request):
    return render(request, 'home.html')


def create_employee_post(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            obj = Employee()
            obj.name = form.cleaned_data['name']
            obj.age = form.cleaned_data['age']
            obj.email = form.cleaned_data['email']
            obj.address = form.cleaned_data['address']
            obj.save()
            return HttpResponseRedirect("/")
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', context={'form': form})


def employee_list(request):
    data = Employee.objects.all()
    return render(request, 'employee_list.html', context={'query_set': data})
