from django.urls import path, include
from . import views

app_name = 'departament_app'

urlpatterns = [
    path('new-department/', views.NewDepartmentView.as_view(), name ='new-deparment'),
    path('list-department/', views.DepartamentListView.as_view(), name ='list-deparment')
]
