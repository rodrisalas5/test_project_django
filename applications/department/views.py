from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .forms import NewDepartmentForm
from .models import Department
from applications.person.models import Employee

class NewDepartmentView(FormView):
    template_name = 'department/new_department.html'
    form_class = NewDepartmentForm
    success_url = '/'

    # def valid(self, form):
    #     return super(NewDepartmentForm, self).form_valid(form)

    def form_valid(self, form):
        print("Estamos en el form valid")
        depa = Department(
            # Atributos del modelo = A lo que definimos en el formulario y pedimos en el HTML
            name_deparment = form.cleaned_data['name_deparment'],
            short_name = form.cleaned_data['short_name'],
        )

        depa.save()

        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']

        Employee.objects.create(
            name = name,
            last_name = last_name,
            position = '3',
            department = depa,
        )
        return super(NewDepartmentView, self).form_valid(form)
    

class DepartamentListView(ListView):
    model = Department
    template_name = 'department/list.html'
    context_object_name = 'departaments'