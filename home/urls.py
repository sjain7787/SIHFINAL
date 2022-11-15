from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" , views.index,name='home'),
    path("contact" , views.contact,name='contact'),
    path("shippro" , views.shippro,name='shippro'),
    path("services" , views.service,name='services'),
    path("import" , views.import1,name='import'),
    path("feedback",views.feedback,name='feedback'),
    path("about",views.about,name='about'),
    path("login",views.loginuser,name='login'),
    path("logout",views.logoutuser,name='logout'),
    path("export",views.export1,name='export'),
    path("portoperations",views.portoperations,name='portoperations'),
    path("employeecorner",views.employeecorner,name='employeecorner'),
    path("logistics",views.logistics,name='logistics'),
    path("immigrations",views.immigrations,name='immigrations'),
    path("customs",views.customs,name='customs'),
    path("boehome",views.boehome,name='boehome'),
    path("boewarehousing",views.boewarehousing,name='boewarehousing'),
    path("boeexhome",views.boeexhome,name='boeexhome'),
    path("integration",views.integration,name='integration'),
    path("auditing",views.auditing,name='auditing'),
    path("companyaudit",views.companyaudit,name='companyaudit'),
    path("shipaudit",views.shipcaudit,name='shipaudit'),
    path("portaudit",views.portcaudit,name='portaudit'),
]
