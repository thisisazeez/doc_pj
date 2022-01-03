from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .forms import *
from app.models import CustomUser, Sop,  Staffs, Departments, Intakes, Finance, Product


def staff_home(request):
    return render(request, "staff_template/staff_home_template.html")#, context


# #department
def add_department(request):
    return render(request, "staff_template/add_department_template.html")

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
    return render(request, 'staff_template/manage_department_template.html', context)

def edit_department(request, department_id):
    department = Departments.objects.get(id=department_id)
    context = {
        "department": department,
        "id": department_id
    }
    return render(request, 'staff_template/edit_department_template.html', context)

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



# #intake
def add_intake(request):
    return render(request, "staff_template/add_intake_template.html")

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
    return render(request, 'staff_template/manage_intake_template.html', context)

def edit_intake(request, intake_id):
    intake = Intakes.objects.get(id=intake_id)
    context = {
        "intake": intake,
        "id": intake_id
    }
    return render(request, 'staff_template/edit_intake_template.html', context)

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


# Sop and Shits


# # Product view
# def create_product(request):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Sop.objects.count()

#     product = ProductForm()

#     if request.method == "POST":
#         product = ProductForm(request.POST)
#         if product.is_valid():
#             product.save()
#             return redirect("staff_create_product")

#     context = {
#         "total_product": total_product,
#         # "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "product": product,
#     }

#     return render(request, "staff_template/create_product.html", context)


# def view_product(request):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Sop.objects.count()

#     product = Product.objects.filter(product_is_delete=False)

#     context = {
#         "total_product": total_product,
#         # "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "product": product,
#     }

#     return render(request, "staff_template/view_product.html", context)


# # Edit product
# def edit_product(request, pk):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()

#     product = Product.objects.get(id=pk)
#     form = ProductForm(instance=product)

#     if request.method == "POST":
#         # customer = CustomerForm(request.POST, instance=product)
#         if form.is_valid():
#             product.save()
#             return redirect("staff_view_product")

#     context = {
#         "total_product": total_product,
#         # "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "product": form,
#     }

#     return render(request, "staff_template/create_product.html", context)


# # Delete product
# def delete_product(request, pk):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()

#     product = Product.objects.get(id=pk)

#     if request.method == "POST":
#         product.product_is_delete = True
#         product.save()
#         return redirect("staff_view_product")

#     context = {
#         "total_product": total_product,
#         # "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "product": product,
#     }

#     return render(request, "staff_template/delete_product.html", context)


# # invoice


# # Invoice view
# def create_invoice(request):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Sop.objects.count()

#     form = SopInvoiceForm()
#     formset = SopDetailFormSet()
#     if request.method == "POST":
#         form = SopInvoiceForm(request.POST)
#         formset = SopDetailFormSet(request.POST)
#         if form.is_valid():
#             invoice = Sop.objects.create(
#                 customer=form.cleaned_data.get("customer"),
#                 date=form.cleaned_data.get("date"),
#             )
#         if formset.is_valid():
#             total = 0
#             for form in formset:
#                 product = form.cleaned_data.get("product")
#                 amount = form.cleaned_data.get("amount")
#                 if product and amount:
#                     # Sum each row
#                     sum = float(product.product_price) * float(amount)
#                     # Sum of total invoice
#                     total += sum
#                     SopDetail(
#                         sop=invoice, product=product, amount=amount
#                     ).save()
#             # Pointing the customer
#             points = 0
#             if total > 1000:
#                 points += total / 1000
#             invoice.customer.customer_points = round(points)
#             # Save the points to Customer table
#             invoice.save()

#             # Save the invoice
#             invoice.total = total
#             invoice.save()
#             return redirect("staff_view_invoice")

#     context = {
#         "total_product": total_product,
#         # "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "form": form,
#         "formset": formset,
#     }

#     return render(request, "staff_template/create_invoice.html", context)


# def view_invoice(request):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()

#     invoice = Invoice.objects.all()

#     context = {
#         "total_product": total_product,
#         # "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "invoice": invoice,
#     }

#     return render(request, "staff_template/view_invoice.html", context)


# # Detail view of invoices
# def view_invoice_detail(request, pk):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Sop.objects.count()

#     invoice = Sop.objects.get(id=pk)
#     invoice_detail = SopDetail.objects.filter(sop=invoice)

#     context = {
#         "total_product": total_product,
#         # "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         'invoice': invoice,
#         "invoice_detail": invoice_detail,
#     }

#     return render(request, "staff_template/view_invoice_detail.html", context)


# # Delete invoice
# def delete_invoice(request, pk):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()

#     invoice = Invoice.objects.get(id=pk)
#     invoice_detail = InvoiceDetail.objects.filter(invoice=invoice)
#     if request.method == "POST":
#         invoice_detail.delete()
#         invoice.delete()
#         return redirect("staff_view_invoice")

#     context = {
#         "total_product": total_product,
#         # "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "invoice": invoice,
#         "invoice_detail": invoice_detail,
#     }

#     return render(request, "staff_template/delete_invoice.html", context)

def staff_profile(request):
    pass