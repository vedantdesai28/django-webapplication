from django.contrib import admin
from django.urls import path, include

import bookinginfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookinginfo.urls'))

]
