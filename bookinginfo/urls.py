from django.urls import path

from bookinginfo.views import (

    LocationList,
    ServiceList, BusList,
    SemesterList,
    UserList,
    EnrollmentList,
    LocationDetails,
    ServiceDetail,
    SemesterDetail,
    UserDetail, EnrollmentDetail, BusDetail
)

urlpatterns = [
    path('location/',
         LocationList.as_view(),
         name='bookinginfo_location_list_urlpattern'),

    path('location/<int:pk>/',
         LocationDetails.as_view(),
         name='bookinginfo_location_detail_urlpattern'),

    path('service/',
         ServiceList.as_view(),
         name='bookinginfo_service_list_urlpattern'),

    path('service/<int:pk>/',
         ServiceDetail.as_view(),
         name='bookinginfo_service_detail_urlpattern'),

    path('bus/',
         BusList.as_view(),
         name='bookinginfo_bus_list_urlpattern'),

    path('bus/<int:pk>/',
         BusDetail.as_view(),
         name='bookinginfo_bus_detail_urlpattern'),

    path('semester/',
         SemesterList.as_view(),
         name='bookinginfo_semester_list_urlpattern'),

    path('semester/<int:pk>/',
         SemesterDetail.as_view(),
         name='bookinginfo_semester_detail_urlpattern'),

    path('user/',
         UserList.as_view(),
         name='bookinginfo_user_list_urlpattern'),

    path('user/<int:pk>/',
         UserDetail.as_view(),
         name='bookinginfo_user_detail_urlpattern'),

    #     path('enrollment/', enrollment_list_view),
    #
    path('enrollment/',
         EnrollmentList.as_view(),
         name='bookinginfo_enrollment_list_urlpattern'),

    path('enrollment/<int:pk>/',
         EnrollmentDetail.as_view(),
         name='bookinginfo_enrollment_detail_urlpattern'),

]
