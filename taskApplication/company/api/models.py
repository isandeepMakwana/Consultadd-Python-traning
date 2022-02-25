from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Department(models.Model):
    dept_id = models.IntegerField()
    dept_name = models.CharField(max_length=100, primary_key=True,default="NONE")
    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    salary = models.IntegerField()
    department = models.ForeignKey(Department , on_delete=models.PROTECT)
    def __str__(self):
        return self.emp_name

