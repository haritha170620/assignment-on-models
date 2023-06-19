from django.db import models

# Create your models here.

class Department(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    dept_location=models.CharField(max_length=100)

    def __str__ (self) -> str:
        return self. dept_no
        return self.dept_name
        return self.dept_location


class Employee(models.Model):
    dept_no=models.ForeignKey(Department,on_delete=models.CASCADE)
    emp_no=models.IntegerField()
    emp_name=models.CharField(max_length=100)

    def __str__ (self) -> str:
        return self.emp_no
        return self.emp_name


    
