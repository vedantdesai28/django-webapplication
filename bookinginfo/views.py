from django.shortcuts import render, get_object_or_404
from django.views import View

from bookinginfo.models import (
    LocationDetail,
    BusName,
    Enrollment,
    Semester,
    User,
    Service,
)


class LocationList(View):

    def get(self, request):
        return render(
            request,
            'bookinginfo/location_list.html',
            {'location_list': LocationDetail.objects.all()}
        )


class LocationDetails(View):

    def get(self, request, pk):
        location = get_object_or_404(
            LocationDetail,
            pk=pk
        )
        service_list_start = location.startlocation.all()
        service_list_end = location.endlocation.all()
        return render(
            request,
            'bookinginfo/location_detail.html',
            {'location': location, 'service_list': service_list_start, 'service_list_2': service_list_end}
        )


class ServiceList(View):

    def get(self, request):
        return render(
            request,
            'bookinginfo/service_list.html',
            {'service_list': Service.objects.all()}
        )


class ServiceDetail(View):

    def get(self, request, pk):
        service = get_object_or_404(
            Service,
            pk=pk
        )
        bus = service.bus
        start_location = service.start_location
        end_location = service.end_location
        trip_direction = service.trip_direction
        semester = service.semester
        enrollment_list = service.enrollments.all()
        return render(
            request,
            'bookinginfo/service_detail.html',
            {'service': service,
             'bus': bus,
             'start_location': start_location,
             'end_location': end_location,
             'trip_direction': trip_direction,
             'semester': semester,
             'enrollment_list': enrollment_list}
        )


class BusList(View):

    def get(self, request):
        return render(
            request,
            'bookinginfo/busname_list.html',
            {'bus_list': BusName.objects.all()}
        )


class BusDetail(View):

    def get(self, request, pk):
        bus = get_object_or_404(
            BusName,
            pk=pk
        )

        bus_name = bus.bus_name
        bus_number = bus.bus_number
        service_list = bus.schedules.all()
        return render(
            request,
            'bookinginfo/busname_detail.html',
            {
                'bus': bus,
                'bus_name': bus_name,
                'bus_number': bus_number,
                'service_list': service_list
            }
        )


class SemesterList(View):

    def get(self, request):
        return render(
            request,
            'bookinginfo/semester_list.html',
            {'semester_list': Semester.objects.all()}
        )


class SemesterDetail(View):

    def get(self, request, pk):
        semester = get_object_or_404(
            Semester,
            pk=pk
        )

        service_list = semester.schedules.all()
        return render(
            request,
            'bookinginfo/semester_detail.html',
            {
                'semester': semester,
                'section_list': service_list}
        )


class UserList(View):

    def get(self, request):
        return render(
            request,
            'bookinginfo/user_list.html',
            {'user_list': User.objects.all()}
        )


class UserDetail(View):

    def get(self, request, pk):
        user = get_object_or_404(
            User,
            pk=pk
        )

        service_list = user.enrollments.all()
        return render(
            request,
            'bookinginfo/user_detail.html',
            {
                'user': user,
                'service_list': service_list}
        )


class EnrollmentList(View):

    def get(self, request):
        return render(
            request,
            'bookinginfo/enrollment_list.html',
            {'enrollment_list': Enrollment.objects.all()}
        )


class EnrollmentDetail(View):

    def get(self, request, pk):
        enrollment = get_object_or_404(
            Enrollment,
            pk=pk
        )

        user = enrollment.user
        service = enrollment.service
        return render(
            request,
            'bookinginfo/enrollment_detail.html',
            {
                'enrollment': enrollment,
                'user': user,
                'service': service
            }
        )
