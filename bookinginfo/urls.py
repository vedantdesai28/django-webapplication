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
    path('locationdetail/', location_list_view),
    path('service/', service_list_view),
    path('bus/', bus_list_view),
    path('semester/', semester_list_view),
    path('user/', user_list_view),
    path('enrollment/', enrollment_list_view),

]
