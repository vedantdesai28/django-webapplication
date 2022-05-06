from django.contrib import admin

from django.urls import path, include
from .views import redirect_root_view

import bookinginfo

urlpatterns = [
    path('', redirect_root_view),
    path('admin/', admin.site.urls),
    path('', include('bookinginfo.urls'))

]
