from django.contrib import admin
from .models import Students, User, Cons, Reciept, Invoice, Intakes, Departments, student_status, feeType, Paymenttype, Programme, staffDepartments
# Register your models here.


admin.site.register(User)
admin.site.register(Departments)
admin.site.register(feeType)
admin.site.register(Programme)
admin.site.register(Paymenttype)
admin.site.register(Intakes)
admin.site.register(Cons)
admin.site.register(student_status)
admin.site.register(Students)