from django.db import models

class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    

    def __str__(self):
        return f"{self.emp_id} - {self.name}"
