from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Semester, Period, Year, Enrollment, Service, User, LocationDetail, BusName

admin.site.register(Period)
admin.site.register(Year)
admin.site.register(BusName)
admin.site.register(Enrollment)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(LocationDetail)
admin.site.register(Semester)

