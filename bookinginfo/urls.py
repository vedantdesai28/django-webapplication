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
    UserDetail,
    EnrollmentDetail,
    BusDetail,
    LocationCreate,
    ServiceCreate,
    BusCreate,
    SemesterCreate,
    EnrollmentCreate,
    UserCreate,
    LocationUpdate,
    ServiceUpdate,
    BusUpdate, SemesterUpdate, UserUpdate, EnrollmentUpdate
)

urlpatterns = [
    path('location/',
         LocationList.as_view(),
         name='bookinginfo_location_list_urlpattern'),

    path('location/<int:pk>/',
         LocationDetails.as_view(),
         name='bookinginfo_location_detail_urlpattern'),

    path('location/create/',
         LocationCreate.as_view(),
         name='bookinginfo_location_create_urlpattern'),

    path('location/<int:pk>/update/',
         LocationUpdate.as_view(),
         name='bookinginfo_location_update_urlpattern'),

    path('service/',
         ServiceList.as_view(),
         name='bookinginfo_service_list_urlpattern'),

    path('service/<int:pk>/',
         ServiceDetail.as_view(),
         name='bookinginfo_service_detail_urlpattern'),

    path('service/create/',
         ServiceCreate.as_view(),
         name='bookinginfo_service_create_urlpattern'),

    path('service/<int:pk>/update/',
         ServiceUpdate.as_view(),
         name='bookinginfo_service_update_urlpattern'),

    path('bus/',
         BusList.as_view(),
         name='bookinginfo_bus_list_urlpattern'),

    path('bus/create/',
         BusCreate.as_view(),
         name='bookinginfo_bus_create_urlpattern'),

    path('bus/<int:pk>/',
         BusDetail.as_view(),
         name='bookinginfo_bus_detail_urlpattern'),

    path('bus/<int:pk>/update/',
         BusUpdate.as_view(),
         name='bookinginfo_bus_update_urlpattern'),

    path('semester/',
         SemesterList.as_view(),
         name='bookinginfo_semester_list_urlpattern'),

    path('semester/<int:pk>/',
         SemesterDetail.as_view(),
         name='bookinginfo_semester_detail_urlpattern'),

    path('semester/create/',
         SemesterCreate.as_view(),
         name='bookinginfo_semester_create_urlpattern'),

    path('semester/<int:pk>/update/',
         SemesterUpdate.as_view(),
         name='bookinginfo_semester_update_urlpattern'),

    path('user/',
         UserList.as_view(),
         name='bookinginfo_user_list_urlpattern'),

    path('user/<int:pk>/',
         UserDetail.as_view(),
         name='bookinginfo_user_detail_urlpattern'),

    path('user/create/',
         UserCreate.as_view(),
         name='bookinginfo_user_create_urlpattern'),

    path('user/<int:pk>/update/',
         UserUpdate.as_view(),
         name='bookinginfo_user_update_urlpattern'),

    path('enrollment/',
         EnrollmentList.as_view(),
         name='bookinginfo_enrollment_list_urlpattern'),

    path('enrollment/<int:pk>/',
         EnrollmentDetail.as_view(),
         name='bookinginfo_enrollment_detail_urlpattern'),

    path('enrollment/create/',
         EnrollmentCreate.as_view(),
         name='bookinginfo_enrollment_create_urlpattern'),

    path('enrollment/<int:pk>/enrollment/',
         EnrollmentUpdate.as_view(),
         name='bookinginfo_enrollment_update_urlpattern'),

]
