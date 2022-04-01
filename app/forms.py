from django import forms
from django.forms import widgets
from .models import *
import json
from django.forms import formset_factory
#Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from app.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    nin = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    phone_num = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'nin','phone_num','email', 'password1', 'password2', 'is_admin', 'is_registrar1', 'is_registrar2', 'is_cashier', 'is_expenses', 'is_expenses_admin', 'is_daily_report', 'is_weekly_report', 'is_monthly_report', 'is_expenses_report', 'is_add', 'is_issue', 'is_expenses_admin')

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'student',
            'date',
            'paymentTerms',
            'status',
            'type',
            'amount',
        ]
        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_student_name',
                'name': 'invoice_student_name',
            }),
            'paymentTerms': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_paymentTerms_name',
                'name': 'invoice_paymentTerms_name',
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_type_name',
                'name': 'invoice_type_name',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_status_name',
                'name': 'invoice_status_name',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'invoice_date',
                'placeholder': 'Enter date create',
                'type': 'date',
                'name': 'invoice_date',
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_amount',
                'placeholder': '0',
                'type': 'number',
            }),
        }

class DetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = [
            'amount',
        ]
        widgets = {
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_detail_amount',
                'placeholder': '0',
                'type': 'number',
            })
        }

DetailFormSet = formset_factory(DetailForm, extra=1)

# SOP


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_price',
            'product_unit',
        ]
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product_name',
                'placeholder': 'Enter name of the product',
            }),
            'product_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'product_price',
                'placeholder': 'Enter price of the product',
                'type': 'number',
            }),
            'product_unit': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product_unit',
                'placeholder': 'Enter unit of the product',
            }),
        }


class SopInvoiceForm(forms.ModelForm):
    class Meta:
        model = Sop
        fields = [
            'customer',
            'date',
        ]
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_customer_name',
                'name': 'invoice_customer_name',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'invoice_date',
                'placeholder': 'Enter date create',
                'type': 'date',
                'name': 'invoice_date',
            }),
        }


class SopDetailForm(forms.ModelForm):
    class Meta:
        model = SopDetail
        fields = [
            'product',
            'amount',
        ]
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_detail_product',
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_detail_amount',
                'placeholder': '0',
                'type': 'number',
            })
        }

SopDetailFormSet = formset_factory(SopDetailForm, extra=1)



# class ClientForm(forms.ModelForm):
#     class Meta:
#         model = Students
#         fields = ['username', 'last_name', 'first_name', 'address', 'email']



# class InvoiceForm(forms.ModelForm):
#     THE_OPTIONS = [
#     ('14 days', '14 days'),
#     ('30 days', '30 days'),
#     ('60 days', '60 days'),
#     ]
#     STATUS_OPTIONS = [
#     ('CURRENT', 'CURRENT'),
#     ('OVERDUE', 'OVERDUE'),
#     ('PAID', 'PAID'),
#     ]

#     title = forms.CharField(
#                     required = True,
#                     label='Invoice Name or Title',
#                     widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Title'}),)
#     paymentTerms = forms.ChoiceField(
#                     choices = THE_OPTIONS,
#                     required = True,
#                     label='Select Payment Terms',
#                     widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
#     status = forms.ChoiceField(
#                     choices = STATUS_OPTIONS,
#                     required = True,
#                     label='Change Invoice Status',
#                     widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
#     notes = forms.CharField(
#                     required = True,
#                     label='Enter any notes for the client',
#                     widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

#     dueDate = forms.DateField(
#                         required = True,
#                         label='Invoice Due',
#                         widget=DateInput(attrs={'class': 'form-control mb-3'}),)


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('title', css_class='form-group col-md-6'),
#                 Column('dueDate', css_class='form-group col-md-6'),
#                 css_class='form-row'),
#             Row(
#                 Column('paymentTerms', css_class='form-group col-md-6'),
#                 Column('status', css_class='form-group col-md-6'),
#                 css_class='form-row'),
#             'notes',

#             Submit('submit', ' EDIT INVOICE '))

#     class Meta:
#         model = Invoice
#         fields = ['title', 'dueDate', 'paymentTerms', 'status', 'notes']


# class SettingsForm(forms.ModelForm):
#     class Meta:
#         model = Settings
#         fields = ['username', 'last_name', 'first_name', 'address', 'email']


# class ClientSelectForm(forms.ModelForm):

#     def __init__(self,*args,**kwargs):
#         self.initial_client = kwargs.pop('initial_client')
#         self.CLIENT_LIST = Students.objects.all()
#         self.CLIENT_CHOICES = [('-----', '--Select a Client--')]


#         for client in self.CLIENT_LIST:
#             d_t = (client.id, client.username)
#             self.CLIENT_CHOICES.append(d_t)


#         super(ClientSelectForm,self).__init__(*args,**kwargs)

#         self.fields['client'] = forms.ChoiceField(
#                                         label='Choose a related client',
#                                         choices = self.CLIENT_CHOICES,
#                                         widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

#     class Meta:
#         model = Invoice
#         fields = ['client']


#     def clean_client(self):
#         c_client = self.cleaned_data['client']
#         if c_client == '-----':
#             return self.initial_client
#         else:
#             return Students.objects.get(id=c_client)





















# <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
# <input type="password" class="form-control" id="floatingPassword" placeholder="Password">