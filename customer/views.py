import email
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import *
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework import viewsets
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import time
from datetime import datetime,timedelta,date
# Create your views here.


@csrf_exempt
def customer_signup(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        Serializers = CustomerInfoSerializers(data=jsonData)
        if Serializers.is_valid():
            Serializers.save()
            return JsonResponse({"status":"success","message":"saved successfully"})
        return JsonResponse({"status":"failure","message":"request not valid"})

@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        customer_check = CustomerInfo.objects.filter(email=jsonData["email"],password=jsonData["password"])
        if customer_check.exists():
            customer = CustomerInfo.objects.get(email=jsonData["email"])
            data = CustomerInfoSerializers(customer,many=False)
            return JsonResponse({"status":"success","message":"retrived successfully","details":data.data})




class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = EnquiryInfo.objects.all()
    serializer_class = EnquiryInfoSerializers

    def post(self, request, *args, **kwargs):
        brand = request.data["brand"]
        car_model = request.data["car_model"]
        manufacture_year = request.data["manufacture_year"]
        parts_name = request.data["parts_name"]
        title = request.data["title"]
        customer_id = int(request.data["customer_id"]) 
        img = request.data["img"]
        EnquiryInfo.objects.create(brand=brand,car_model=car_model,manufacture_year=manufacture_year,parts_name=parts_name,parts_image=img,title=title,customer_id=customer_id)
        return JsonResponse({"status":"success","message":"enquiry created"})

@csrf_exempt
def enquiry_create(request):
    if request.method == 'POST':
        brand = request.POST["brand"]
        car_model = request.POST["car_model"]
        manufacture_year = request.POST["manufacture_year"]
        parts_name = request.POST["parts_name"]
        title = request.POST["title"]
        customer_id = int(request.POST["customer_id"]) 
        img = request.POST["img"]
        EnquiryInfo.objects.create(brand=brand,car_model=car_model,manufacture_year=manufacture_year,parts_name=parts_name,parts_image=img,title=title,customer_id=customer_id)
        return JsonResponse({"status":"success","message":"enquiry created"})


@csrf_exempt
def enquiry_list_by_customer(request,pk):
    if request.method == 'GET':
        enq = EnquiryInfo.objects.filter(customer_id=pk)
        jsondata = EnquiryInfoSerializers(enq,many=True)
        return JsonResponse({"status":"success","message":"enquiry list","enquiry_list":jsondata.data[::-1]}) 

@csrf_exempt
def new_enquiry_list(request):
    if request.method == 'GET':
        enq = EnquiryInfo.objects.filter(status="pending")
        jsondata = EnquiryInfoSerializers(enq,many=True)
        return JsonResponse({"status":"success","message":"enquiry list","enquiry_list":jsondata.data}) 

@csrf_exempt
def enquiry_detail_by_id(request,pk):
    if request.method == 'GET':
        enq = EnquiryInfo.objects.get(id=pk)
        jsondata = EnquiryInfoSerializers(enq,many=False)
        return JsonResponse({"status":"success","message":"enquiry list","enquiry_list":jsondata.data}) 



# print(type(customer_id))

        # filePath = FileSystemStorage(location=settings.STORAGE_PATH)
        # fileName = ""
        # for i in request.FILES:
        #     file = request.FILES[i]
        #     print(file)
        #     ts = time.time()
        #     fileName = str(ts)+"_"+str(file)
        #     path = filePath.save(fileName, ContentFile(file.read()))
        #     fileName = settings.STORAGE_PATH+fileName
        # data = {
        #     "brand":brand,
        #     "car_model":car_model,
        #     "manufacture_year":manufacture_year,
        #     "parts_name":parts_name,
        #     "title":title,
        #     "customer_id":customer_id,
        #     "parts_image":fileName
        # }
        # print(data)
        # Serializers = EnquiryInfoSerializers(data=data)
        # if Serializers.is_valid():
        #     Serializers.save()
        #     return JsonResponse({"status":"success","message":"saved successfully"})
        # return JsonResponse({"status":"failure","message":"request not valid"})