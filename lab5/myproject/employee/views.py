from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
import datetime

def check_promotion(request):
    if request.method == "GET":
        emp_id = request.GET.get('emp_id')
        employee = Employee.objects.filter(emp_id=emp_id).first()
        if employee:
            experience = (datetime.date.today() - employee.date_of_joining).days // 365
            return JsonResponse({"eligible": "YES" if experience >= 5 else "NO"})
    return JsonResponse({"eligible": "NO"})

def promotion_form(request):
    employees = Employee.objects.all()
    return render(request, 'promotion.html', {'employee': employees})
