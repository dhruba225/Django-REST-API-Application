from django.urls import path, include
from api.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)


urlpatterns=[
  # for home page
  path('home',home,name='home'),

  # for apis
  path('',include(router.urls))

]