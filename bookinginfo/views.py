from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from bookinginfo.forms import LocationForm, ServiceForm, BusForm, SemesterForm, EnrollmentForm, UserForm
from bookinginfo.models import (
    LocationDetail,
    BusName,
    Enrollment,
    Semester,
    User,
    Service,
)
from bookinginfo.utils import ObjectCreateMixin


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


class LocationCreate(ObjectCreateMixin, View):
    form_class = LocationForm
    template_name = 'bookinginfo/location_form.html'


class LocationUpdate(View):
    form_class = LocationForm
    model = LocationDetail
    template_name = 'bookinginfo/location_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        location = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=location),
            'location': location,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        location = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=location)
        if bound_form.is_valid():
            new_instructor = bound_form.save()
            return redirect(new_instructor)
        else:
            context = {
                'form': bound_form,
                'location': location,
            }
            return render(
                request,
                self.template_name,
                context)


# class InstructorDelete(View):
#
#     def get(self, request, pk):
#         instructor = self.get_object(pk)
#         sections = instructor.sections.all()
#         if sections.count() > 0:
#             return render(
#                 request,
#                 'courseinfo/instructor_refuse_delete.html',
#                 {'instructor': instructor,
#                  'sections': sections,
#                  }
#             )
#         else:
#             return render(
#                 request,
#                 'courseinfo/instructor_confirm_delete.html',
#                 {'instructor': instructor}
#             )
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             Instructor,
#             pk=pk)
#
#     def post(self, request, pk):
#         instructor = self.get_object(pk)
#         instructor.delete()
#         return redirect('courseinfo_instructor_list_urlpattern')


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


class ServiceUpdate(View):
    form_class = ServiceForm
    model = Service
    template_name = 'bookinginfo/service_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        service = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=service),
            'service': service,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        service = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=service)
        if bound_form.is_valid():
            new_section = bound_form.save()
            return redirect(new_section)
        else:
            context = {
                'form': bound_form,
                'section': service,
            }
            return render(
                request,
                self.template_name,
                context)


class ServiceCreate(ObjectCreateMixin, View):
    form_class = ServiceForm
    template_name = 'bookinginfo/service_form.html'


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


class BusCreate(ObjectCreateMixin, View):
    form_class = BusForm
    template_name = 'bookinginfo/bus_form.html'


class BusUpdate(View):
    form_class = BusForm
    model = BusName
    template_name = 'bookinginfo/bus_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        bus = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=bus),
            'service': bus,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        bus = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=bus)
        if bound_form.is_valid():
            new_section = bound_form.save()
            return redirect(new_section)
        else:
            context = {
                'form': bound_form,
                'bus': bus,
            }
            return render(
                request,
                self.template_name,
                context)


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


class SemesterCreate(ObjectCreateMixin, View):
    form_class = SemesterForm
    template_name = 'bookinginfo/semester_form.html'


class SemesterUpdate(View):
    form_class = SemesterForm
    model = Semester
    template_name = 'bookinginfo/semester_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        semester = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=semester),
            'semester': semester,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        semester = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=semester)
        if bound_form.is_valid():
            new_semester = bound_form.save()
            return redirect(new_semester)
        else:
            context = {
                'form': bound_form,
                'semester': semester,
            }
            return render(
                request,
                self.template_name,
                context)

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


class UserCreate(ObjectCreateMixin, View):
    form_class = UserForm
    template_name = 'bookinginfo/user_form.html'


class UserUpdate(View):
    form_class = UserForm
    model = User
    template_name = 'bookinginfo/user_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=user),
            'user': user,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        user = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=user)
        if bound_form.is_valid():
            new_semester = bound_form.save()
            return redirect(new_semester)
        else:
            context = {
                'form': bound_form,
                'user': user,
            }
            return render(
                request,
                self.template_name,
                context)


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


class EnrollmentCreate(ObjectCreateMixin, View):
    form_class = EnrollmentForm
    template_name = 'bookinginfo/enrollment_form.html'


class EnrollmentUpdate(View):
    form_class = EnrollmentForm
    model = Enrollment
    template_name = 'bookinginfo/enrollment_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        enrollment = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=enrollment),
            'enrollment': enrollment,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        enrollment = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=enrollment)
        if bound_form.is_valid():
            new_semester = bound_form.save()
            return redirect(new_semester)
        else:
            context = {
                'form': bound_form,
                'enrollment': enrollment,
            }
            return render(
                request,
                self.template_name,
                context)

