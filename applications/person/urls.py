from django.urls import path, include
from .models import Employee
from . import views
from .views import ListAllEmployee, SuccessView, ListByDepartment, EmployeeCreateView


# class EmployeeConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'applications.person'

app_name = 'person_app'

urlpatterns = [
    path('all-employees/', views.ListAllEmployee.as_view(), name = 'all_employees'),
    path('SuccessView/', views.SuccessView.as_view(), name = 'correct'),
    # path('ListByDepartmentFinances/', views.ListByDepartment.as_view()),
    path('two-employees/', views.ListAllEmployeeByFour.as_view()),
    path('ListByDepartment/<short_name>', views.ListByDepartment.as_view(), name = 'listByDepartment'),
    path('ListByWord/', views.ListByDepartmentByWord.as_view()),
    path('ListEmployeeAbility/', views.ListAbilityEmployeeWithIdOne.as_view()),
    path('EmployeeDetailView/<pk>', views.EmployeeDetailView.as_view()),
    path('EmployeeDetailViewKwargs/<pk>', views.EmployeeDetailViewKwargs.as_view(), name='empleado_detail'),
    path('addEmployee/', views.EmployeeCreateView.as_view(), name='add_employee'),
    path('EditEmployee/<pk>/', views.EmployeeUpdateView.as_view(), name='modify_employee'),
    path('DeleteEmployee/<pk>/', views.DeleteEmployeeView.as_view(), name='delete_employee'),
    path('', views.InicioView.as_view(), name='Inicio'),
    path('list-employees-admin/', views.ListEmployeeAdmin.as_view(), name='list-employees-admin')
]
