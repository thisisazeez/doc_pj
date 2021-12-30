
from django.urls import path, include

from . import views
from .import HodViews, StaffViews, FinanceViews


urlpatterns = [
    path('', views.loginPage, name="login"),
    #  path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),


    # URLS for Staff
    path('staff_home/', StaffViews.staff_home, name="staff_home"),

    # URSL for Finance
    path('finance_home/', FinanceViews.finance_home, name="finance_home"),

]