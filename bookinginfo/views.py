from django.shortcuts import render

from bookinginfo.models import (
    LocationDetail,
    BusName,
    Enrollment,
    Semester,
    User,
    Service,
)


def location_list_view(request):
    location_list = LocationDetail.objects.all()
    # instructor_list = Instructor.objects.none()
    return render(request, 'bookinginfo/location_list.html', {'location_list': location_list})


def service_list_view(request):
    service_list = Service.objects.all()
    # section_list = Section.objects.none()
    return render(request, 'bookinginfo/service_list.html', {'service_list': service_list})


def bus_list_view(request):
    bus_list = BusName.objects.all()
    # course_list = Course.objects.none()
    return render(request, 'bookinginfo/busname_list.html', {'bus_list': bus_list})


def semester_list_view(request):
    semester_list = Semester.objects.all()
    # semester_list = Semester.objects.none()
    return render(request, 'bookinginfo/semester_list.html', {'semester_list': semester_list})


def user_list_view(request):
    user_list = User.objects.all()
    # student_list = Student.objects.none()
    return render(request, 'bookinginfo/user_list.html', {'user_list': user_list})


def enrollment_list_view(request):
    enrollment_list = Enrollment.objects.all()
    # registration_list = Registration.objects.none()
    return render(request, 'bookinginfo/enrollment_list.html', {'enrollment_list': enrollment_list})
