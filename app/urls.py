
from django.urls import path, include

from . import views
from .import HodViews, StaffViews, FinanceViews


urlpatterns = [
    path('', views.login_view, name="login"),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('report/', HodViews.SimpleListReport.as_view(), name="report_gen"),
      # Admin Staff
    # path('report_engine/', HodViews.MyReport.as_view(), name="report_engine"),
     # Admin Student
    path('add_student/', HodViews.add_student, name="add_student"),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    path('manage_student/', HodViews.manage_student, name="manage_student"),
    path('edit_student/<stu_id>/', HodViews.edit_student, name="edit_student"),
    path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    path('delete_student/<stu_id>/', HodViews.delete_student, name="delete_student"),


    path('response/', HodViews.excelview, name="response_excel"),
    path('add_ptype/', HodViews.add_ptype, name="add_ptype"),
    path('add_ptype_save/', HodViews.add_ptype_save, name="add_ptype_save"),
    path('manage_ptype/', HodViews.manage_ptype, name="manage_ptype"),
    path('edit_ptype/<ptype_id>/', HodViews.edit_ptype, name="edit_ptype"),
    path('edit_ptype_save/', HodViews.edit_ptype_save, name="edit_ptype_save"),
    path('delete_ptype/<ptype_id>/', HodViews.delete_ptype, name="delete_ptype"),


    path('add_department/', HodViews.add_department, name="add_department"),
    path('add_department_save/', HodViews.add_department_save, name="add_department_save"),
    path('manage_department/', HodViews.manage_department, name="manage_department"),
    path('edit_department/<department_id>/', HodViews.edit_department, name="edit_department"),
    path('edit_department_save/', HodViews.edit_department_save, name="edit_department_save"),
    path('delete_department/<department_id>/', HodViews.delete_department, name="delete_department"),

    path('add_department_st/', HodViews.add_department_st, name="add_department_st"),
    path('add_department_st_save/', HodViews.add_department_st_save, name="add_department_st_save"),
    path('manage_department_st/', HodViews.manage_department_st, name="manage_department_st"),
    path('edit_department_st/<department_id>/', HodViews.edit_department_st, name="edit_department_st"),
    path('edit_department_st_save/', HodViews.edit_department_save, name="edit_department_st_save"),
    path('delete_department_st/<department_id>/', HodViews.delete_department, name="delete_department_st"),


    path('add_fee_type/', HodViews.add_fee_type, name="add_fee_type"),
    path('add_fee_type_save/', HodViews.add_fee_type_save, name="add_fee_type_save"),
    path('manage_fee_type/', HodViews.manage_fee_type, name="manage_fee_type"),
    path('edit_fee_type/<fee_id>/', HodViews.edit_fee_type, name="edit_fee_type"),
    path('edit_fee_type_save/', HodViews.edit_fee_type_save, name="edit_fee_type_save"),
    path('delete_fee_type/<fee_id>/', HodViews.delete_fee_type, name="delete_fee_type"),

    path('add_programme/', HodViews.add_programme, name="add_programme"),
    path('add_programme_save/', HodViews.add_programme_save, name="add_programme_save"),
    path('manage_programme/', HodViews.manage_programme, name="manage_programme"),
    path('edit_programme/<programme_id>/', HodViews.edit_programme, name="edit_programme"),
    path('edit_programme_save/', HodViews.edit_programme_save, name="edit_programme_save"),
    path('delete_programme/<programme_id>/', HodViews.delete_programme, name="delete_programme"),


    path('manage_sop_admin/', HodViews.manage_sop_admin, name="manage_sop_admin"),
    path('edit_sop_admin/<sop_id>/', HodViews.edit_sop_admin, name="edit_sop_admin"),
    path('edit_sop_admin_save/', HodViews.edit_sop_admin_save, name="edit_sop_admin_save"),
    path('delete_sop_admin/<sop_id>/', HodViews.delete_sop_admin, name="delete_sop_admin"),

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
    path('add_sop/', StaffViews.add_sop, name="add_sop"),
    path('add_sop_save/', StaffViews.add_sop_save, name="add_sop_save"),
    path('manage_sop/', StaffViews.manage_sop, name="manage_sop"),
    path('edit_sop/<sop_id>/', StaffViews.edit_sop, name="edit_sop"),
    path('edit_sop_save/', StaffViews.edit_sop_save, name="edit_sop_save"),
    path('delete_sop/<sop_id>/', StaffViews.delete_sop, name="delete_sop"),
    
    
    # URSL for Finance
    path('search_/', FinanceViews.SearchResultsView.as_view(), name="finance_search_result"),
    path('search_stu/', FinanceViews.search, name="finance_search"),
    path('finance_home/', FinanceViews.finance_home, name="finance_home"),
    path('finance_profile/', FinanceViews.finance_profile, name="finance_profile"),
    path('payslip/<int:pk>/', FinanceViews.payslip, name='dashboard_payslip'),
    # path('invoices/create',FinanceViews.createInvoice, name='create-invoice'),
    path('create_invoice/', FinanceViews.create_invoice, name='create_invoice'),
    path('view_invoice/', FinanceViews.view_invoice, name='view_invoice'),
    path('delete_invoice/<int:pk>/', FinanceViews.delete_invoice, name='delete_invoice'),
    path('finance_dashboard/venue_pdf/', FinanceViews.venue_pdf, name='venue_pdf'),
    path('view_invoice_detail/<int:pk>/', FinanceViews.view_invoice_detail, name='view_invoice_detail'),
    path('add_reciept/<student_id>/', FinanceViews.add_reciept, name="add_reciept"),
    path('add_reciept_save/', FinanceViews.add_reciept_save, name="add_reciept_save"),
    path('manage_reciept/', FinanceViews.manage_reciept, name="manage_reciept"),
    path('edit_reciept/<reciept_id>/', FinanceViews.edit_reciept, name="edit_reciept"),
    path('create_pdf/<reciept_id>/', FinanceViews.pdf_report_create, name="pdf_report_create"),
    path('_pdf/<reciept_id>/', FinanceViews.pdf__create, name="pdf__create"),
    path('edit_reciept_save/', FinanceViews.edit_reciept_save, name="edit_reciept_save"),
    path('delete_reciept/<reciept_id>/', FinanceViews.delete_reciept, name="delete_reciept"),
   

]