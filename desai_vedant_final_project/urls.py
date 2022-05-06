"""desai_vedant_final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from bookinginfo.views import (
    location_list_view,
    service_list_view,
    bus_list_view,
    enrollment_list_view,
    semester_list_view,
    user_list_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/', location_list_view),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locationdetail/', location_list_view),
    path('service/', service_list_view),
    path('bus/', bus_list_view),
    path('semester/', semester_list_view),
    path('user/', user_list_view),
    path('enrollment/', enrollment_list_view),

]
