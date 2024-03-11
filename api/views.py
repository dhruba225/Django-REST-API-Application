from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from api.models import Company
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

# views for home page

def home(request):
  print("home page requested")
  friends = [
    'lulu',
    'papuni',
    'jaga'
  ]
  return JsonResponse(friends,safe=False)



# views for apis
class CompanyViewSet(viewsets.ModelViewSet):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer


  # companies/{companyID}/employees
  @action(detail=True,methods=['get'])
  def employees(self,request,pk=None):
    try:
      company = Company.objects.get(pk = pk)
      emps = Employee.objects.filter(company = company)
      emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
      return Response(emps_serializer.data)
    except Exception as e:
      print(e)
      return Response('Company Does Not Exit')

      

class EmployeeViewSet(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer