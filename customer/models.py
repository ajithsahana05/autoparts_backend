
from django.db import models

# Create your models here.
def upload_path(instance, filname):
    return '/'.join(['enquiry', str(instance.title), filname])


class CustomerInfo(models.Model):
    name = models.CharField(max_length=45,null=True)
    gender = models.CharField(max_length=30,null=True)
    mobile_no = models.CharField(max_length=15)
    email = models.CharField(max_length=30,unique=True)
    is_admin = models.BooleanField(default=False,null=True)
    password = models.CharField(max_length=45,null=True)


class EnquiryInfo(models.Model):
    brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    manufacture_year = models.CharField(max_length=20)
    parts_name = models.CharField(max_length=30)
    parts_image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    status = models.CharField(max_length=30,default="pending")
    title = models.CharField(max_length=30)
    customer_id = models.ForeignKey(CustomerInfo,on_delete=models.CASCADE)


class SupplierInfo(models.Model):
    supplier_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30,unique=True)
    mobile_no = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)

class QuotationInfo(models.Model):
    enquiry_id = models.ForeignKey(EnquiryInfo,on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(SupplierInfo,on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)