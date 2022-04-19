from rest_framework import serializers
from .models import *


class CustomerInfoSerializers(serializers.ModelSerializer):
    class Meta():
        model = CustomerInfo
        fields = "__all__"

class EnquiryInfoSerializers(serializers.ModelSerializer):
    class Meta():
        model = EnquiryInfo
        fields = "__all__"