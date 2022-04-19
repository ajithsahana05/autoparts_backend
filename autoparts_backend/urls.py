"""autoparts_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from customer import views 
from rest_framework import routers
from customer.views import EnquiryViewSet
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register('enquiry/add', EnquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('customer/add',views.customer_signup),
    path('login/api',views.login_api),
    path('customer/enquiry/list/<int:pk>',views.enquiry_list_by_customer),
    path('new/enquiry/list',views.new_enquiry_list),
    path('enquiry/detail/<int:pk>',views.enquiry_detail_by_id),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)