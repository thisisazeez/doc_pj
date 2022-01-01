from django import forms
from django.forms import widgets
from .models import *
import json

#Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Colum



class ClientForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['username', 'last_name', 'first_name', 'address', 'email']



class InvoiceForm(forms.ModelForm):
    THE_OPTIONS = [
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]
    STATUS_OPTIONS = [
    ('CURRENT', 'CURRENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title = forms.CharField(
                    required = True,
                    label='Invoice Name or Title',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Title'}),)
    paymentTerms = forms.ChoiceField(
                    choices = THE_OPTIONS,
                    required = True,
                    label='Select Payment Terms',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    status = forms.ChoiceField(
                    choices = STATUS_OPTIONS,
                    required = True,
                    label='Change Invoice Status',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    notes = forms.CharField(
                    required = True,
                    label='Enter any notes for the client',
                    widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

    dueDate = forms.DateField(
                        required = True,
                        label='Invoice Due',
                        widget=DateInput(attrs={'class': 'form-control mb-3'}),)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('dueDate', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('paymentTerms', css_class='form-group col-md-6'),
                Column('status', css_class='form-group col-md-6'),
                css_class='form-row'),
            'notes',

            Submit('submit', ' EDIT INVOICE '))

    class Meta:
        model = Invoice
        fields = ['title', 'dueDate', 'paymentTerms', 'status', 'notes']


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['username', 'last_name', 'first_name', 'address', 'email']


class ClientSelectForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        self.initial_client = kwargs.pop('initial_client')
        self.CLIENT_LIST = Students.objects.all()
        self.CLIENT_CHOICES = [('-----', '--Select a Client--')]


        for client in self.CLIENT_LIST:
            d_t = (client.id, client.username)
            self.CLIENT_CHOICES.append(d_t)


        super(ClientSelectForm,self).__init__(*args,**kwargs)

        self.fields['client'] = forms.ChoiceField(
                                        label='Choose a related client',
                                        choices = self.CLIENT_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    class Meta:
        model = Invoice
        fields = ['client']


    def clean_client(self):
        c_client = self.cleaned_data['client']
        if c_client == '-----':
            return self.initial_client
        else:
            return Students.objects.get(id=c_client)





















# <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
# <input type="password" class="form-control" id="floatingPassword" placeholder="Password">