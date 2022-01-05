from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField
from app.models import CustomUser,  Staffs, Departments, Intakes, Cons,Finance, Students, student_status, Reciept


def admin_home(request):
   return render(request, "hod_template/home_content.html")#,context

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)

def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')
    
def staff_profile(request):
    pass

def finance_profile(requtest):
    pass

#staff
def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = "lincolnstaff12345"
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_staff')

def manage_staff(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request, "hod_template/manage_staff_template.html", context)

def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)

    context = {
        "staff": staff,
        "id": staff_id
    }
    return render(request, "hod_template/edit_staff_template.html", context)

def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            if password != None and password != "":
                user.set_password(password)
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Staff Updated Successfully.")
            return redirect('/edit_staff/'+staff_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/'+staff_id)

def delete_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "Staff Deleted Successfully.")
        return redirect('manage_staff')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_staff')




#finance
def add_finance(request):
    return render(request, "hod_template/add_finance_template.html")

def add_finance_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_finance')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = "lincolnfinance12345"
        address = request.POST.get('address')

        # try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
        user.finance.address = address
        user.save()
        messages.success(request, "finance Added Successfully!")
        return redirect('add_finance')
        # except:
        #     messages.error(request, "Failed to Add finance!")
        #     return redirect('add_finance')

def manage_finance(request):
    finance = Finance.objects.all()
    context = {
        "finance": finance,
    }
    return render(request, "hod_template/manage_finance_template.html", context)

def edit_finance(request, finance_id):
    finance = Finance.objects.get(admin=finance_id)

    context = {
        "finance": finance,
        "id": finance_id
    }
    return render(request, "hod_template/edit_finance_template.html", context)

def edit_finance_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        finance_id = request.POST.get('finance_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=finance_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            if password != None and password != "":
                user.set_password(password)
            user.username = username
            user.save()
            
            # INSERTING into finance Model
            finance_model = Finance.objects.get(admin=finance_id)
            finance_model.address = address
            finance_model.save()

            messages.success(request, "finance Updated Successfully.")
            return redirect('/edit_finance/'+finance_id)

        except:
            messages.error(request, "Failed to Update finance.")
            return redirect('/edit_finance/'+finance_id)

def delete_finance(request, finance_id):
    finance = Finance.objects.get(admin=finance_id)
    try:
        finance.delete()
        messages.success(request, "finance Deleted Successfully.")
        return redirect('manage_finance')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_staff')



# #students

def add_student(request):
    #student = Students.objects.get(admin=student_id)
    departments = Departments.objects.all()
    intakes = Intakes.objects.all()
    status = student_status.objects.all()

    context = {
        "departments":departments,
        "intakes":intakes,
        "status":status,
        #"student": student,
        #"student_id": student_id
    }
    return render(request, 'hod_template/add_student_template.html', context)

def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_student')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        intake = request.POST.get('intake')
        department = request.POST.get('department')
        status = request.POST.get('status')



        user = Students.objects.create(username=username, email=email, 
        last_name=last_name, first_name=first_name)
        # user.department=Departments.objects.get(id=department) 
        # user.intake=Intakes.objects.get(id=intake)
        # user.status=student_status.objects.get(status_name=status)
        user.address = address
        user.save()
        messages.success(request, "student Added Successfully!")
        return redirect('add_student')

def manage_student(request):
    students = Students.objects.all()
    context = {
        "students": students
    }
    return render(request, "hod_template/manage_student_template.html", context)

def edit_student(request, student_id):
    student = Students.objects.get(id=student_id)
    departments = Departments.objects.all()
    intakes = Intakes.objects.all()
    status = student_status.objects.all()

    context = {
        "departments":departments,
        "intakes":intakes,
        "status":status,
        "student": student,
        "student_id": student_id
    }
    return render(request, "hod_template/edit_student_template.html", context)

def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        intake = request.POST.get('intake')
        status = request.POST.get('status')
        gender = request.POST.get('gender')


        user = Students.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()
        
        # INSERTING into student Model
        print(department)
        student_model = Students.objects.get(id=student_id)
        student_model.department=Departments.objects.get(id=department) 
        student_model.intake=Intakes.objects.get(id=intake)
        student_model.status=student_status.objects.get(id=status)
        student_model.gender=gender
        student_model.address = address
        student_model.save()

        messages.success(request, "student Updated Successfully.")
        return redirect('/edit_student/'+student_id)

def delete_student(request, student_id):
    student = Students.objects.get(id=student_id)
    try:
        student.delete()
        messages.success(request, "student Deleted Successfully.")
        return redirect('manage_student')
    except:
        messages.error(request, "Failed to Delete student.")
        return redirect('manage_student')


def add_department(request):
    return render(request, "hod_template/add_department_template.html")

def add_department_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_department')
    else:
        department = request.POST.get('department')
        try:
            department_model = Departments(department_name=department)
            department_model.save()
            messages.success(request, "Department Added Successfully!")
            return redirect('add_department')
        except:
            messages.error(request, "Failed to Add Department!")
            return redirect('add_department')

def manage_department(request):
    departments = Departments.objects.all()
    context = {
        "departments": departments
    }
    return render(request, 'hod_template/manage_department_template.html', context)

def edit_department(request, department_id):
    department = Departments.objects.get(id=department_id)
    context = {
        "department": department,
        "id": department_id
    }
    return render(request, 'hod_template/edit_department_template.html', context)

def edit_department_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        department_id = request.POST.get('department_id')
        department_name = request.POST.get('department')

        try:
            department = Departments.objects.get(id=department_id)
            department.department_name = department_name
            department.save()

            messages.success(request, "department Updated Successfully.")
            return redirect('/edit_department/'+department_id)

        except:
            messages.error(request, "Failed to Update department.")
            return redirect('/edit_department/'+department_id)

def delete_department(request, department_id):
    department = Departments.objects.get(id=department_id)
    try:
        department.delete()
        messages.success(request, "department Deleted Successfully.")
        return redirect('manage_department')
    except:
        messages.error(request, "Failed to Delete department.")
        return redirect('manage_department')

# Status

def add_status(request):
    return render(request, "hod_template/add_status_template.html")

def add_status_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_status')
    else:
        status = request.POST.get('status')
        try:
            status_model = student_status(status_name=status)
            status_model.save()
            messages.success(request, "status Added Successfully!")
            return redirect('add_status')
        except:
            messages.error(request, "Failed to Add status!")
            return redirect('add_status')

def manage_status(request):
    status = student_status.objects.all()
    context = {
        "status": status
    }
    return render(request, 'hod_template/manage_status_template.html', context)

def edit_status(request, status_id):
    status = student_status.objects.get(id=status_id)
    context = {
        "status": status,
        "id": status_id
    }
    return render(request, 'hod_template/edit_status_template.html', context)

def edit_status_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        status_id = request.POST.get('status_id')
        status_name = request.POST.get('status')

        try:
            status = student_status.objects.get(id=status_id)
            status.status_name = status_name
            status.save()

            messages.success(request, "status Updated Successfully.")
            return redirect('/edit_status/'+status_id)

        except:
            messages.error(request, "Failed to Update status.")
            return redirect('/edit_status/'+status_id)

def delete_status(request, status_id):
    status = student_status.objects.get(id=status_id)
    try:
        status.delete()
        messages.success(request, "status Deleted Successfully.")
        return redirect('manage_status')
    except:
        messages.error(request, "Failed to Delete status.")
        return redirect('manage_status')

# Intakes

def add_intake(request):
    return render(request, "hod_template/add_intake_template.html")

def add_intake_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_intake')
    else:
        intake = request.POST.get('intake')
        try:
            intake_model = Intakes(intake_name=intake)
            intake_model.save()
            messages.success(request, "intake Added Successfully!")
            return redirect('add_intake')
        except:
            messages.error(request, "Failed to Add intake!")
            return redirect('add_intake')

def manage_intake(request):
    intakes = Intakes.objects.all()
    context = {
        "intakes": intakes
    }
    return render(request, 'hod_template/manage_intake_template.html', context)

def edit_intake(request, intake_id):
    intake = Intakes.objects.get(id=intake_id)
    context = {
        "intake": intake,
        "id": intake_id
    }
    return render(request, 'hod_template/edit_intake_template.html', context)

def edit_intake_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        intake_id = request.POST.get('intake_id')
        intake_name = request.POST.get('intake')

        try:
            intake = Intakes.objects.get(id=intake_id)
            intake.intake_name = intake_name
            intake.save()

            messages.success(request, "intake Updated Successfully.")
            return redirect('/edit_intake/'+intake_id)

        except:
            messages.error(request, "Failed to Update intake.")
            return redirect('/edit_intake/'+intake_id)

def delete_intake(request, intake_id):
    intake = Intakes.objects.get(id=intake_id)
    try:
        intake.delete()
        messages.success(request, "intake Deleted Successfully.")
        return redirect('manage_intake')
    except:
        messages.error(request, "Failed to Delete intake.")
        return redirect('manage_intake')


@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

# SOP Admin


def manage_sop_admin(request):
    sops = Cons.objects.all()
    context = {
        "sops": sops
    }
    return render(request, 'hod_template/manage_sop_template.html', context)

def edit_sop_admin(request, sop_id):
    sop = Cons.objects.get(id=sop_id)
    context = {
        "sop": sop,
        "id": sop_id,
    }
    return render(request, 'hod_template/edit_sop_template.html', context)

def edit_sop_admin_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        sop_id = request.POST.get('sop_id')
        item_1 = request.POST.get('item_1')
        i_price_1 = request.POST.get('i_price_1')
        item_2 = request.POST.get('item_2')
        i_price_2 = request.POST.get('i_price_2')
        item_3 = request.POST.get('item_3')
        i_price_3 = request.POST.get('i_price_3')
        item_4 = request.POST.get('item_4')
        i_price_4 = request.POST.get('i_price_4')
        item_5 = request.POST.get('item_5')
        i_price_5 = request.POST.get('i_price_5')
        is_approved= request.POST.get('is_approved')
        if is_approved == 'on':
            is_approved = True
        else:
            is_approved = False
        # try:
        sop = Cons.objects.get(id=sop_id)
        sop.one = item_1
        sop.amountOne = i_price_1
        sop.two = item_2
        sop.amountTwo = i_price_2
        sop.three = item_3
        sop.amountThree = i_price_3
        sop.four = item_4
        sop.amountFour = i_price_4
        sop.five = item_5
        sop.amountFive = i_price_5
        sop.is_approved = is_approved
        sop.save()

        messages.success(request, "SOP Updated Successfully.")
        return redirect('/edit_sop_admin/'+sop_id)

        # except:
        #     messages.error(request, "Failed to Update SOP.")
        #     return redirect('/edit_sop_admin/'+sop_id)

def delete_sop_admin(request, sop_id):
    sop = Cons.objects.get(id=sop_id)
    try:
        sop.delete()
        messages.success(request, "SOP Deleted Successfully.")
        return redirect('manage_sop_admin')
    except:
        messages.error(request, "Failed to Delete SOP.")
        return redirect('manage_sop_admin')


class SimpleListReport(SlickReportView):
    
    report_model = Reciept
    # the model containing the data we want to analyze

    date_field = 'date'
    # a date/datetime field on the report model

    # fields on the report model ... surprise !
    columns = ['date', 'student_name', 'student_id', 'tution', 'acceptance', 'application', 'others','amount', 'total']
