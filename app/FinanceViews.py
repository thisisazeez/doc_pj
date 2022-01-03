from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .models import CustomUser,  Staffs, Departments, Intakes, Finance, Students, Invoice, InvoiceDetail
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
