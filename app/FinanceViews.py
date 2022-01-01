from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from app.models import CustomUser,  Staffs, Departments, Intakes, Finance


def finance_home(request):
    return render(request, "finance_template/finance_home_template.html")#, context

def finance_profile(request):
    pass

