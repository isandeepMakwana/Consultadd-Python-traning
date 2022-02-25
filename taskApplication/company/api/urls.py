
from django.urls import path
from .views import Employees ,SingleEmployee
urlpatterns = [
    path('employees' ,Employees.as_view()),
    path('employees/<int:id>' ,SingleEmployee.as_view()),

]
