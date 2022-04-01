from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q
from django.views.generic import ListView
import json
from .models import Paymenttype, Reciept, Departments, Intakes, Students, Invoice, InvoiceDetail, feeType
from .forms import  InvoiceForm
import os
from uuid import uuid4
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib.staticfiles import finders


def finance_home(request):
    return render(request, "finance_template/finance_home_template.html")#, context

def finance_profile(request):
    pass


def venue_pdf(request):
    buf = io.BytesIO()

    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    # lines = [
    #     "Hi Evevery One",
    #     "Hi Evevery One",
    #     "Hi Evevery One",
    # ]

    receipt = InvoiceDetail.objects.all().get(id=id)

    lines = []

    for rc in receipt:
        lines.append(rc.invoice)
        lines.append(rc.amount)
        lines.append(" ")






    # for line in lines:
    #     textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='reciept.pdf')

def payslip(request, pk):
    student = Students.objects.get(id=pk)
    template_path = 'finance_template/student_payslip.html'
    context = {
        'student': student,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# def createInvoice(request):
#     #create a blank invoice ....
#     # number = 'INV-'+str(uuid4()).split('-')[-1]
#     newInvoice = Invoice.objects.create()#number=number
#     newInvoice.save()

#     inv = Invoice.objects.get()#number=number
#     return redirect('create-build-invoice', slug=inv.slug)



def create_invoice(request):
    total_students = Students.objects.count()
    total_invoice = Invoice.objects.count()

    form = InvoiceForm()
    # formset = InvoiceDetailFormSet()
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        # formset = InvoiceDetailFormSet(request.POST)
        if form.is_valid():
            invoice = Invoice.objects.create(
                student=form.cleaned_data.get("student"),
                date=form.cleaned_data.get("date"),
                status=form.cleaned_data.get("status"),
                type=form.cleaned_data.get("type"),
                paymentTerms=form.cleaned_data.get("paymentTerms"),
                amount=form.cleaned_data.get("amount"),

            )
        # if formset.is_valid():
            # total = 0
            # for form in formset:
                # product = form.cleaned_data.get("product")
                # amount = form.cleaned_data.get("amount")
                # if product and amount:
                #     # Sum each row
                #     sum = float(product.product_price) * float(amount)
                #     # Sum of total invoice
                #     total += sum
                #amountamount
            InvoiceDetail(
                invoice=invoice,
            ).save()
            # Pointing the customer
            # points = 0
            # if total > 1000:
            #     points += total / 1000
            # invoice.customer.customer_points = round(points)
            # Save the points to Customer table
            invoice.student.save()

            # Save the invoice
            # invoice.total = total
            invoice.save()
            return redirect("view_invoice")

    context = {
        "total_students": total_students,
        "total_invoice": total_invoice,
        "form": form,
        # "formset": formset,
    }

    return render(request, "finance_template/create_invoice.html", context)


def view_invoice(request):
    total_students = Students.objects.count()
    total_invoice = Invoice.objects.count()

    invoice = Invoice.objects.all()

    context = {
        "total_students": total_students,
        "total_invoice": total_invoice,
        "invoice": invoice,
    }

    return render(request, "finance_template/view_invoice.html", context)


# Detail view of invoices
def view_invoice_detail(request, pk):
    total_students = Students.objects.count()
    total_invoice = Invoice.objects.count()

    invoice = Invoice.objects.get(id=pk)
    invoice_detail = InvoiceDetail.objects.filter(invoice=invoice)

    context = {
        "total_students": total_students,
        "total_invoice": total_invoice,
        # 'invoice': invoice,
        "invoice_detail": invoice_detail,
    }

    return render(request, "finance_template/view_invoice_detail.html", context)


# Delete invoice
def delete_invoice(request, pk):
    total_students = Students.objects.count()
    total_invoice = Invoice.objects.count()

    invoice = Invoice.objects.get(id=pk)
    invoice_detail = InvoiceDetail.objects.filter(invoice=invoice)
    if request.method == "POST":
        invoice_detail.delete()
        invoice.delete()
        return redirect("view_invoice")

    context = {
        "total_students": total_students,
        "total_invoice": total_invoice,
        "invoice": invoice,
        "invoice_detail": invoice_detail,
    }

    return render(request, "finance_template/delete_invoice.html", context)





# Recipet O.G

def add_reciept(request, student_id):
    student = Students.objects.get(id=student_id)
    ptype = Paymenttype.objects.all()
    ftype = feeType.objects.all()
    context = {
        "student": student,
        "ptype": ptype,
        "ftype": ftype,
        "id": student_id,
    }
    return render(request, "finance_template/add_reciept_template.html", context)

def add_reciept_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('manage_reciept')
    else:
        stu_name = request.POST.get('stu_name')
        stu_id = request.POST.get('stu_id')
        student_id = request.POST.get('student_id')
        ptype = request.POST.get('ptype')
        # tution = request.POST.get('tution')
        # if tution == 'on':
        #     tution = True
        # else:
        #     tution = False
        # acceptance = request.POST.get('acceptance')
        # if acceptance == 'on':
        #     acceptance = True
        # else:
        #     acceptance = False
        # application = request.POST.get('application')
        # if application == 'on':
        #     application = True
        # else:
        #     application = False
        # others = request.POST.get('others')
        # if others == 'on':
        #     others = True
        # else:
        #     others = False
        amount = request.POST.get('amount')
        balance = request.POST.get('balance')
        stu_nin = request.POST.get('stu_nin')
        ftype = request.POST.get('ftype')
        stu_programme = request.POST.get('stu_programme')
        total = request.POST.get('total')
        notes = request.POST.get('notes')

        try:
            reciept_model = Reciept(student_name=stu_name, student_id=stu_id,
            amount=amount, total=total, notes=notes, balance=balance,
            student_nin=stu_nin, stu_programme=stu_programme)
            reciept_model.ptype=Paymenttype.objects.get(id=ptype)
            reciept_model.ftype=feeType.objects.get(id=ftype)
            reciept_model.save()
            messages.success(request, "Reciept Added Successfully!")
            return redirect('/add_reciept/'+student_id)
        except:
            messages.error(request, "Failed to Add Recipt!")
            return redirect('/add_reciept/'+student_id)


def manage_reciept(request):
    rec = Reciept.objects.all()
    context = {
        "rec": rec
    }
    return render(request, 'finance_template/manage_reciept_template.html', context)

def edit_reciept(request, reciept_id):
    reciept = Reciept.objects.get(id=reciept_id)
    context = {
        "reciept": reciept,
        "id": reciept_id,
    }
    return render(request, 'finance_template/edit_reciept_template.html', context)

class SearchResultsView(ListView):
    model = Students
    template_name = 'finance_template/search_results.html'

    def get_queryset(self):
        query= self.request.GET.get('q')
        object_list = Students.objects.filter(
            Q(student_id__icontains=query) | Q(nin__icontains=query) | Q(ip_id__icontains=query)
        )
        return object_list

def search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = Students.objects.filter(Q(student_id__icontains=query) | Q(nin__icontains=query) | Q(ip_id__icontains=query) | Q(first_name__icontains=query) | Q(email__icontains=query))

    return render(request, 'finance_template/search.html', {'query': query, 'results': results})

def pdf_report_create(request, reciept_id):
    reciept = Reciept.objects.get(id=reciept_id)
    context = {
        "reciept": reciept,
        "id": reciept_id,
    }
    template_path = 'finance_template/PdfReciept.html'
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="stu_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
# Try All
def pdf__create(request, reciept_id):
    reciept = Reciept.objects.get(id=reciept_id)
    context = {
        "reciept": reciept,
        "id": reciept_id,
    }
    return render(request, 'finance_template/reprint.html', context)


def edit_reciept_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:        
        stu_name = request.POST.get('stu_name')
        stu_id = request.POST.get('stu_id')
        reciept_id = request.POST.get('reciept_id')
        tution = request.POST.get('tution')
        if tution == 'on':
            tution = True
        else:
            tution = False
        acceptance = request.POST.get('acceptance')
        if acceptance == 'on':
            acceptance = True
        else:
            acceptance = False
        application = request.POST.get('application')
        if application == 'on':
            application = True
        else:
            application = False
        others = request.POST.get('others')
        if others == 'on':
            others = True
        else:
            others = False
        amount = request.POST.get('amount')
        total = request.POST.get('total')
        notes = request.POST.get('notes')
        try:
            rec = Reciept.objects.get(id=reciept_id)
            rec.student_name = stu_name
            rec.student_id = stu_id
            rec.tution = tution
            rec.acceptance = acceptance
            rec.application = application
            rec.others = others
            rec.amount = amount
            rec.total = total
            rec.notes = notes
            rec.save()

            messages.success(request, "Reciept Updated Successfully.")
            return redirect('/edit_reciept/'+reciept_id)

        except:
            messages.error(request, "Failed to Update Reciept.")
            return redirect('/edit_reciept/'+reciept_id)

def delete_reciept(request, reciept_id):
    reciept = Reciept.objects.get(id=reciept_id)
    try:
        reciept.delete()
        messages.success(request, "Reciept Deleted Successfully.")
        return redirect('manage_reciept')
    except:
        messages.error(request, "Failed to Delete Reciept.")
        return redirect('manage_reciept')
