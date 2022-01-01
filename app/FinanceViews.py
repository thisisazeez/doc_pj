from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from app.models import CustomUser,  Staffs, Departments, Intakes, Finance, Students, Invoice
import os
from uuid import uuid4
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


def finance_home(request):
    return render(request, "finance_template/finance_home_template.html")#, context

def finance_profile(request):
    pass


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



def createInvoice(request):
    #create a blank invoice ....
    # number = 'INV-'+str(uuid4()).split('-')[-1]
    newInvoice = Invoice.objects.create()#number=number
    newInvoice.save()

    inv = Invoice.objects.get()#number=number
    return redirect('create-build-invoice', slug=inv.slug)

