from django.contrib import admin
from django.urls import include, path
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

# router 
router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)
urlpatterns = [
    path('',include(router.urls))
]
