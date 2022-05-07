from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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


class LocationDetails(DetailView):
    model = LocationDetail

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        location = self.get_object()
        service_list_start = location.startlocation.all()
        service_list_end = location.endlocation.all()
        context['service_list'] = service_list_start
        context['service_list_2'] = service_list_end
        return context


class LocationCreate(ObjectCreateMixin, View):
    form_class = LocationForm
    template_name = 'bookinginfo/locationdetail_form.html'


class LocationUpdate(UpdateView):
    form_class = LocationForm
    model = LocationDetail
    template_name = 'bookinginfo/locationdetail_form_update.html'


class LocationDelete(View):

    def get(self, request, pk):
        location = self.get_object(pk)
        services1 = location.startlocation.all()
        services2 = location.endlocation.all()
        if services1.count() > 0 or services2.count() > 0:
            return render(
                request,
                'bookinginfo/locationdetail_refuse_delete.html',
                {'location': location,
                 'services_start': services1,
                 'services_end': services2,
                 }
            )
        else:
            return render(
                request,
                'bookinginfo/locationdetail_confirm_delete.html',
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
    model = Service


class ServiceDetail(DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        service = self.get_object()
        bus = service.bus
        start_location = service.start_location
        end_location = service.end_location
        trip_direction = service.trip_direction
        semester = service.semester
        enrollment_list = service.enrollments.all()
        context['bus'] = bus
        context['start_location'] = start_location
        context['end_location'] = end_location
        context['trip_direction'] = trip_direction
        context['semester'] = semester
        context['enrollment_list'] = enrollment_list
        return context


class ServiceUpdate(UpdateView):
    form_class = ServiceForm
    model = Service
    template_name = 'bookinginfo/service_form_update.html'


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


class ServiceCreate(CreateView):
    form_class = ServiceForm
    model = Service


class BusList(ListView):
    model = BusName


class BusDetail(DetailView):
    model = BusName

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        bus = self.get_object()
        bus_name = bus.bus_name
        bus_number = bus.bus_number
        service_list = bus.schedules.all()
        context['bus_name'] = bus_name
        context['bus_number'] = bus_number
        context['service_list'] = service_list
        return context


class BusCreate(CreateView):
    form_class = BusForm
    model = BusName


class BusUpdate(UpdateView):
    form_class = BusForm
    model = BusName
    template_name = 'bookinginfo/busname_form_update.html'


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


class SemesterDetail(DetailView):
    model = Semester

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        semester = self.get_object()
        service_list = semester.schedules.all()
        context['section_list'] = service_list
        return context


class SemesterCreate(CreateView):
    form_class = SemesterForm
    model = Semester


class SemesterUpdate(UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = 'bookinginfo/semester_form_update.html'


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


class UserDetail(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        user = self.get_object()
        service_list = user.enrollments.all()
        context['service_list'] = service_list
        return context


class UserCreate(CreateView):
    form_class = UserForm
    model = User


class UserUpdate(UpdateView):
    form_class = UserForm
    model = User
    template_name = 'bookinginfo/user_form_update.html'


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
                'bookinginfo/user_confirm_delete.html',
                {'student': user}
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


class EnrollmentDetail(DetailView):
    model = Enrollment

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        enrollment = self.get_object()
        user = enrollment.user
        service = enrollment.service
        context['user'] = user
        context['service'] = service
        return context


class EnrollmentCreate(CreateView):
    form_class = EnrollmentForm
    model = Enrollment


class EnrollmentUpdate(UpdateView):
    form_class = EnrollmentForm
    model = Enrollment
    template_name = 'bookinginfo/enrollment_form_update.html'


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
        return redirect('bookinginfo_enrollment_list_urlpattern')
