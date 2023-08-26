from django.urls import path

from . import views


urlpatterns = [
    path('',views.employee_form,name='empform'),
    path('list/',views.employee_list,name='emplist'),
     path('<int:id>/',views.employee_form,name='employeeupdate'),
    path('delete/<int:id>',views.employee_delete,name='empdel')
]