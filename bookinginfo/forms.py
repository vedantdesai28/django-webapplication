from django import forms

from bookinginfo.models import LocationDetail, Service, BusName, Semester, User, Enrollment


class LocationForm(forms.ModelForm):
    class Meta:
        model = LocationDetail
        fields = '__all__'

    def clean_location_name(self):
        return self.cleaned_data['location_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator']
        return result


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def clean_service_name(self):
        return self.cleaned_data['trip_direction'].strip()


class BusForm(forms.ModelForm):
    class Meta:
        model = BusName
        fields = '__all__'

    def clean_bus_name(self):
        return self.cleaned_data['bus_name'].strip()


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator']
        return result




class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'
