from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from bookinginfo.forms import LocationForm, ServiceForm, BusForm, SemesterForm, EnrollmentForm, UserForm
from bookinginfo.models import (
    LocationDetail,
    BusName,
    Enrollment,
    Semester,
    User,
    Service,
)
from bookinginfo.utils import ObjectCreateMixin, PageLinksMixin


class LocationList(PageLinksMixin, ListView):
    paginate_by = 10
    model = LocationDetail


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


class LocationDelete(View):

    def get(self, request, pk):
        location = self.get_object(pk)
        services1 = location.startlocation.all()
        services2 = location.endlocation.all()
        if services1.count() > 0 or services2.count() > 0:
            return render(
                request,
                'bookinginfo/location_refuse_delete.html',
                {'location': location,
                 'services_start': services1,
                 'services_end': services2,
                 }
            )
        else:
            return render(
                request,
                'bookinginfo/location_confirm_delete.html',
                {'location': location}
            )

    def get_object(self, pk):
        return get_object_or_404(
            LocationDetail,
            pk=pk)

    def post(self, request, pk):
        location = self.get_object(pk)
        location.delete()
        return redirect('bookinginfo_location_list_urlpattern')


class ServiceList(ListView):
    paginate_by = 10
    model = Semester


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


class ServiceDelete(View):

    def get(self, request, pk):
        service = self.get_object(pk)
        enrollment_list = service.enrollments.all()
        if enrollment_list.count() > 0:
            return render(
                request,
                'bookinginfo/service_refuse_delete.html',
                {'service': service,
                 'enrollment': enrollment_list,
                 }
            )
        else:
            return render(
                request,
                'bookinginfo/service_confirm_delete.html',
                {'service': service}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Service,
            pk=pk)

    def post(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return redirect('bookinginfo_service_list_urlpattern')


class ServiceCreate(ObjectCreateMixin, View):
    form_class = ServiceForm
    template_name = 'bookinginfo/service_form.html'


class BusList(ListView):
    model = BusName


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


class BusDelete(View):

    def get(self, request, pk):
        bus = self.get_object(pk)
        service_list = bus.schedules.all()
        if service_list.count() > 0:
            return render(
                request,
                'bookinginfo/bus_refuse_delete.html',
                {'bus': bus,
                 'services': service_list,
                 }
            )
        else:
            return render(
                request,
                'bookinginfo/bus_confirm_delete.html',
                {'bus': bus}
            )

    def get_object(self, pk):
        return get_object_or_404(
            BusName,
            pk=pk)

    def post(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return redirect('bookinginfo_bus_list_urlpattern')


class SemesterList(ListView):
    model = Semester


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


class SemesterDelete(View):

    def get(self, request, pk):
        semester = self.get_object(pk)
        service_list = semester.schedules.all()
        if service_list.count() > 0:
            return render(
                request,
                'bookinginfo/semester_refuse_delete.html',
                {'semester': semester,
                 'services': service_list,
                 }
            )
        else:
            return render(
                request,
                'bookinginfo/semester_confirm_delete.html',
                {'semester': semester}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Semester,
            pk=pk)

    def post(self, request, pk):
        semester = self.get_object(pk)
        semester.delete()
        return redirect('bookinginfo_semester_list_urlpattern')


class UserList(PageLinksMixin, ListView):
    paginate_by = 10
    model = User


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


class UserDelete(View):

    def get(self, request, pk):
        user = self.get_object(pk)
        service_list = user.enrollments.all()
        if service_list.count() > 0:
            return render(
                request,
                'bookinginfo/user_refuse_delete.html',
                {'user': user,
                 'services': service_list,
                 }
            )
        else:
            return render(
                request,
                'bookinginfo/semester_confirm_delete.html',
                {'semester': user}
            )

    def get_object(self, pk):
        return get_object_or_404(
            User,
            pk=pk)

    def post(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return redirect('bookinginfo_user_list_urlpattern')



class EnrollmentList(ListView):
    model = Enrollment


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


class EnrollmentDelete(View):

    def get(self, request, pk):
        enrollment = self.get_object(pk)
        return render(
            request,
            'bookinginfo/enrollment_confirm_delete.html',
            {'enrollment': enrollment}
        )

    def get_object(self, pk):
        enrollment = get_object_or_404(
            Enrollment,
            pk=pk
        )
        return enrollment

    def post(self, request, pk):
        enrollment = self.get_object(pk)
        enrollment.delete()
        return redirect('bookinginfo_enrollment_delete_urlpattern')
