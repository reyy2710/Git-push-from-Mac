from django.urls import path
from employee.views import promotion_form, check_promotion


urlpatterns = [
    path('', promotion_form, name="promotion_form"),
    path('check_promotion/', check_promotion, name="check_promotion"),
]
