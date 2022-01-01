
from django.urls import path, include

from . import views
from .import HodViews, StaffViews, FinanceViews


urlpatterns = [
    path('', views.loginPage, name="login"),
    #  path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),
      # Admin Staff
    path('add_staff/', HodViews.add_staff, name="add_staff"),
    path('add_staff_save/', HodViews.add_staff_save, name="add_staff_save"),
    path('manage_staff/', HodViews.manage_staff, name="manage_staff"),
    path('edit_staff/<staff_id>/', HodViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/', HodViews.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', HodViews.delete_staff, name="delete_staff"),

        # Admin finace
    path('add_finance/', HodViews.add_finance, name="add_finance"),
    path('add_finance_save/', HodViews.add_finance_save, name="add_finance_save"),
    path('manage_finance/', HodViews.manage_finance, name="manage_finance"),
    path('edit_finance/<finance_id>/', HodViews.edit_finance, name="edit_finance"),
    path('edit_finance_save/', HodViews.edit_finance_save, name="edit_finance_save"),
    path('delete_finance/<finance_id>/', HodViews.delete_finance, name="delete_finance"),
     # Admin Student
    path('add_student/', HodViews.add_student, name="add_student"),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    path('manage_student/', HodViews.manage_student, name="manage_student"),
    path('edit_student/<student_id>/', HodViews.edit_student, name="edit_student"),
    path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    path('delete_student/<student_id>/', HodViews.delete_student, name="delete_student"),


    path('add_department/', HodViews.add_department, name="add_department"),
    path('add_department_save/', HodViews.add_department_save, name="add_department_save"),
    path('manage_department/', HodViews.manage_department, name="manage_department"),
    path('edit_department/<department_id>/', HodViews.edit_department, name="edit_department"),
    path('edit_department_save/', HodViews.edit_department_save, name="edit_department_save"),
    path('delete_department/<department_id>/', HodViews.delete_department, name="delete_department"),


    path('add_status/', HodViews.add_status, name="add_status"),
    path('add_status_save/', HodViews.add_status_save, name="add_status_save"),
    path('manage_status/', HodViews.manage_status, name="manage_status"),
    path('edit_status/<status_id>/', HodViews.edit_status, name="edit_status"),
    path('edit_status_save/', HodViews.edit_status_save, name="edit_status_save"),
    path('delete_status/<status_id>/', HodViews.delete_status, name="delete_status"),

    path('add_intake/', HodViews.add_intake, name="add_intake"),
    path('add_intake_save/', HodViews.add_intake_save, name="add_intake_save"),
    path('manage_intake/', HodViews.manage_intake, name="manage_intake"),
    path('edit_intake/<intake_id>/', HodViews.edit_intake, name="edit_intake"),
    path('edit_intake_save/', HodViews.edit_intake_save, name="edit_intake_save"),
    path('delete_intake/<intake_id>/', HodViews.delete_intake, name="delete_intake"),

    # URLS for Staff
    path('staff_home/', StaffViews.staff_home, name="staff_home"),

    # URSL for Finance
    path('finance_home/', FinanceViews.finance_home, name="finance_home"),
    path('admin_profile/', FinanceViews.finance_profile, name="finance_profile"),
    path('payslip/<int:pk>/', FinanceViews.payslip, name='dashboard_payslip'),
    # path('invoices/create',FinanceViews.createInvoice, name='create-invoice'),
    path('create_invoice/', FinanceViews.create_invoice, name='create_invoice'),
    path('view_invoice/', FinanceViews.view_invoice, name='view_invoice'),
    path('delete_invoice/<int:pk>/', FinanceViews.delete_invoice, name='delete_invoice'),
    path('view_invoice_detail/<int:pk>/', FinanceViews.view_invoice_detail, name='view_invoice_detail'),


]