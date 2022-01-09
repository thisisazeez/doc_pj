from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import django
from django.forms import ModelForm
import datetime, calendar
from django import forms
from django.template.defaultfilters import default, slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

class CustomUser(AbstractUser):
    user_type_data = ((1, "management"), (2, "staff"), (3, "finance"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class AdminManagement(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class staffDepartments(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE, blank=True, null=True)
    address = models.TextField()
    nin = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=255)
    ip_id_staff = models.CharField(max_length=255, blank=True, null=True)
    sf_department = models.ForeignKey(staffDepartments, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class Finance(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE, blank=True, null=True)
    address = models.TextField()
    nin = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Intakes(models.Model):
    id = models.AutoField(primary_key=True)
    intake_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Programme(models.Model):
    id = models.AutoField(primary_key=True)
    programme_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Paymenttype(models.Model):
    id = models.AutoField(primary_key=True)
    ptype_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class feeType(models.Model):
    id = models.AutoField(primary_key=True)
    fee_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

# STUDENT_STATUS_CHOICES = (
#     ("applicant", "Applicant"),
#     ("current", "Current"),
# )


class student_status(models.Model):
    id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=50)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, blank=True, null=True)
    intake = models.ForeignKey(Intakes, on_delete=models.CASCADE,blank=True, null=True)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(student_status,on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField()
    gender = models.CharField(max_length=255, blank=True, null=True)
    state_of_origin = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    nxt_of_kin = models.CharField(max_length=255, blank=True, null=True)
    nxt_kin_num = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=255, blank=True, null=True)
    nin = models.CharField(max_length=400, blank=True, null=True)
    ip_id = models.CharField(max_length=400, blank=True, null=True)
    totalFee = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()




class Reciept(models.Model):
    TERMS = [
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]

    TYPE = [
    ('cash', 'cash'),
    ('transfer', 'transfer'),
    ]

    STATUS = [
    ('TUTION', 'TUTION'),
    ('APPLICATION', 'APPLICATION'),
    ('ACCEPTANCE', 'ACCEPTANCE'),
    ('OTHERS', 'OTHERS'),
    ]
    date = models.DateField(auto_now=True, blank=True, null=True)
    # transaction_date = models.DateTimeField(auto_now_add=True, default='', db_index=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.CharField(max_length=255, blank=True, null=True)
    student_nin = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    stu_programme = models.CharField(max_length=255, blank=True, null=True)
    # student = models.ForeignKey(Students, on_delete=models.SET_NULL, blank=True, null=True)
    tution = models.BooleanField(default=False)
    acceptance = models.BooleanField(default=False)
    application = models.BooleanField(default=False)
    others = models.BooleanField(default=False)
    ptype = models.ForeignKey(Paymenttype,on_delete=models.CASCADE, blank=True, null=True)
    # type = models.CharField(choices=TYPE, default='cash', max_length=100)
    amount = models.CharField(blank=True, null=True, max_length=100)
    # paymentTerms = models.CharField(choices=TERMS, default='14 days', max_length=100)
    total = models.FloatField(default=0)
    balance = models.FloatField(default=0)

class Invoice(models.Model):
    TERMS = [
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]

    TYPE = [
    ('cash', 'cash'),
    ('transfer', 'transfer'),
    ]

    STATUS = [
    ('TUTION', 'TUTION'),
    ('APPLICATION', 'APPLICATION'),
    ('ACCEPTANCE', 'ACCEPTANCE'),
    ('OTHERS', 'OTHERS'),
    ]
    date = models.DateField(blank=True, null=True)
    student = models.ForeignKey(Students, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(choices=STATUS, default='TUTION', max_length=100)
    type = models.CharField(choices=TYPE, default='cash', max_length=100)
    amount = models.CharField(blank=True, null=True, max_length=100)
    paymentTerms = models.CharField(choices=TERMS, default='14 days', max_length=100)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.IntegerField(default=0)


# class Invoice(models.Model):
#     TERMS = [
#     ('14 days', '14 days'),
#     ('30 days', '30 days'),
#     ('60 days', '60 days'),
#     ]

#     STATUS = [
#     ('CURRENT', 'CURRENT'),
#     ('OVERDUE', 'OVERDUE'),
#     ('PAID', 'PAID'),
#     ]

#     title = models.CharField(null=True, blank=True, max_length=100)
#     number = models.CharField(null=True, blank=True, max_length=100)
#     dueDate = models.DateField(null=True, blank=True)
#     paymentTerms = models.CharField(choices=TERMS, default='14 days', max_length=100)
#     status = models.CharField(choices=STATUS, default='CURRENT', max_length=100)
#     notes = models.TextField(null=True, blank=True)

#     #RELATED fields
#     client = models.ForeignKey(Students, blank=True, null=True, on_delete=models.SET_NULL)

#     #Utility fields
#     uniqueId = models.CharField(null=True, blank=True, max_length=100)
#     slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     last_updated = models.DateTimeField(blank=True, null=True)


#     def __str__(self):
#         return '{} {}'.format(self.title, self.uniqueId)


#     def get_absolute_url(self):
#         return reverse('invoice-detail', kwargs={'slug': self.slug})


#     def save(self, *args, **kwargs):
#         if self.date_created is None:
#             self.date_created = timezone.localtime(timezone.now())
#         if self.uniqueId is None:
#             self.uniqueId = str(uuid4()).split('-')[4]
#             self.slug = slugify()

#         self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
#         self.last_updated = timezone.localtime(timezone.now())

#         super(Invoice, self).save(*args, **kwargs)


# class Settings(models.Model):

#     # PROVINCES = [
#     # ('Gauteng', 'Gauteng'),
#     # ('Free State', 'Free State'),
#     # ('Limpopo', 'Limpopo'),
#     # ]

#     #Basic Fields
#     clientName = models.CharField(null=True, blank=True, max_length=200)
#     clientLogo = models.ImageField(default='default_logo.jpg', upload_to='company_logos')
#     addressLine1 = models.CharField(null=True, blank=True, max_length=200)
#     phoneNumber = models.CharField(null=True, blank=True, max_length=100)
#     emailAddress = models.CharField(null=True, blank=True, max_length=100)

#     #Utility fields
#     uniqueId = models.CharField(null=True, blank=True, max_length=100)
#     slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     last_updated = models.DateTimeField(blank=True, null=True)


#     def __str__(self):
#         return '{} {} {}'.format(self.clientName, self.province, self.uniqueId)


#     def get_absolute_url(self):
#         return reverse('settings-detail', kwargs={'slug': self.slug})


#     def save(self, *args, **kwargs):
#         if self.date_created is None:
#             self.date_created = timezone.localtime(timezone.now())
#         if self.uniqueId is None:
#             self.uniqueId = str(uuid4()).split('-')[4]
#             self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

#         self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
#         self.last_updated = timezone.localtime(timezone.now())

#         super(Settings, self).save(*args, **kwargs)


# YEAR_CHOICES = []
# for year in range(2021, datetime.datetime.now().year + 1):
#     YEAR_CHOICES.append((year, year))

# MONTHS_CHOICES = tuple(zip(range(1,13), (calendar.month_name[i] for i in range(1,13))))


# class MeltReportForm(forms.Form):
# 	month = forms.ChoiceField(choices=MONTHS_CHOICES)
# 	year = forms.ChoiceField(choices=YEAR_CHOICES)



class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField(default=0)
    product_unit = models.CharField(max_length=255)
    product_is_delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product_name)

class Sop(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Staffs, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)





class Cons(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    one = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=900, blank=True, null=True)
    amountOne = models.CharField(max_length=255, blank=True, null=True)
    two = models.CharField(max_length=255, blank=True, null=True)
    amountTwo = models.CharField(max_length=255, blank=True, null=True)
    three = models.CharField(max_length=255, blank=True, null=True)
    amountThree = models.CharField(max_length=255, blank=True, null=True)
    four = models.CharField(max_length=255, blank=True, null=True)
    amountFour = models.CharField(max_length=255, blank=True, null=True)
    five = models.CharField(max_length=255, blank=True, null=True)
    amountFive = models.CharField(max_length=255, blank=True, null=True)
    is_approved = models.BooleanField(default=False)


class SopDetail(models.Model):
    sop = models.ForeignKey(Sop, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.IntegerField(default=0)

    @property
    def get_total_bill(self):
        total = float(self.product.product_price) * float(self.amount)
        return total

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Finance
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminManagement.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Finance.objects.create(admin=instance) 




@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminmanagement.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.finance.save()



