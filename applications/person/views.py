from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Employee
from django.urls import reverse_lazy
from .forms import EmployeeForm

# Create your views here.
class ListAllEmployee(ListView):
    template_name = "person/list_all.html"
    paginate_by = 5
    model = Employee
    context_object_name = 'employee_list'
    ordering = "name"
    
    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        list = Employee.objects.filter(
            name__icontains = key_word
        )
        return list

class SuccessView(TemplateView):
    template_name = "person/success.html"

# class ListByDepartmentFinances(ListView):
#     template_name = "person/list_area_finances.html"
#     queryset = Employee.objects.filter(department__name='Finances')
#     context_object_name = 'employee_list'

class ListByDepartment(ListView):
    template_name = "person/list_area.html"
    context_object_name = 'employees'
    
    def get_queryset(self):
        area = self.kwargs['short_name']
        employee_list = Employee.objects.filter(department__short_name=area)
        return employee_list
    
class ListByDepartmentByWord(ListView):
    template_name = "person/list_by_word.html"
    context_object_name = 'employee'
    
    
    def get_queryset(self):
        key_word = self.request.GET.get("kword", '') #Etiqueta HTML
        print('========>', key_word)
        employee = Employee.objects.filter(name=key_word)
        print('========> Resutl:', employee)
        print('')
        return employee
    
class ListAllEmployeeByFour(ListView):
    template_name = "person/list_all.html"
    paginate_by = 2
    model = Employee
    ordering = "name"
    context_object_name = 'employee_list'

class ListAbilityEmployeeWithIdOne(ListView):
    template_name = 'person/ability.html'
    context_object_name = 'ability'

    def get_queryset(self):
        employee = Employee.objects.get(id=1)
        return employee.ability.all()
    
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'person/EmployeeDetailView.html'
    context_object_name = 'employee_detail'

class EmployeeDetailViewKwargs(DetailView):
    model = Employee
    template_name = 'person/EmployeeDetailViewKwargs.html'
    context_object_name = 'employee_detail_kwargs'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailViewKwargs, self).get_context_data(**kwargs)
        context['title'] = 'Month employee'
        return context

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'person/addEmployee.html'
    # fields = ('__all__')
    # success_url = '/SuccessView'
    fields = [
        'name',
        'last_name',
        'position',
        'department',
        'ability',
        'avatar'
    ]
    success_url = reverse_lazy('person_app:correct')

    def form_valid(self, form): 
        employee = form.save()
        employee.full_name = employee.name + ' - ' + employee.last_name
        employee.save()
        return super(EmployeeCreateView, self).form_valid(form)
    
class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'person/update.html'
    fields = [
        'name',
        'last_name',
        'position',
        'department',
        'ability',
    ]

    success_url = reverse_lazy('person_app:correct')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # print('********** POST_METHOD **********')
        # print('*********************************')
        print(request.POST)
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        # employee = form.save()
        # employee.full_name = employee.name + ' - ' + employee.last_name
        # employee.save()
        # return super(EmployeeCreateView, self).form_valid(form)
        # print('********** FORM_VALID ***********')
        # print('*********************************')
        return super(EmployeeUpdateView, self).form_valid(form)
    
class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'person/deleteEmployee.html'   
    success_url = reverse_lazy('person_app:correct')

class InicioView(TemplateView):
    template_name = "inicio.html"     

class ListEmployeeAdmin(ListView):
    template_name = 'person/list_employees.html'
    paginate_by = 10
    ordering = 'name'
    context_object_name = 'employees'
    model = Employee

class EmployeeCreateViewForm(CreateView):
    template_name = 'person/add_employee_form.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('person_app:correct')

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.full_name = employee.name + ' ' + employee.last_name
        employee.save()
        return super(EmployeeCreateViewForm, self).form_valid(form)