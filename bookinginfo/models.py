from django.db import models


# Create your models here.
from django.db.models import UniqueConstraint


class Period(models.Model):
    period_id = models.AutoField(primary_key=True)
    period_sequence = models.IntegerField(unique=True)
    period_name = models.CharField(max_length=45, unique=True, default='')

    def __str__(self):
        return '%s' % self.period_name

    class Meta:
        ordering = ['period_sequence']


class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' % self.year

    class Meta:
        ordering = ['year']


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    year = models.ForeignKey(Year, related_name='semesters', on_delete=models.PROTECT)
    period = models.ForeignKey(Period, related_name='semesters', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.year.year, self.period.period_name)

    class Meta:
        ordering = ['year__year', 'period__period_sequence']
        constraints = [
            UniqueConstraint(fields=['year', 'period'], name='unique_semester')
        ]


class BusName(models.Model):
    bus_id = models.AutoField(primary_key=True)
    bus_name = models.CharField(max_length=155)
    bus_number = models.IntegerField(unique=True)

    def __str__(self):
        return '%s - %s' % ( self.bus_number, self.bus_name)

    class Meta:
        ordering = ['bus_number', 'bus_name']
        constraints = [
            UniqueConstraint(fields=['bus_number', 'bus_name'], name='unique_busName')
        ]


class LocationDetail(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    disambiguator = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s' % self.location_name
        else:
            result = '%s (%s)' % (self.location_name, self.disambiguator)
        return result

    class Meta:
        ordering = ['location_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['location_name', 'disambiguator'], name='unique_location')
        ]


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'], name='unique_user')
        ]


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    trip_direction = models.CharField(max_length=45)
    start_location = models.ForeignKey(LocationDetail, related_name='startlocation', on_delete=models.PROTECT)
    end_location = models.ForeignKey(LocationDetail, related_name='endlocation', on_delete=models.PROTECT)
    bus = models.ForeignKey(BusName, related_name='schedules', on_delete=models.PROTECT)
    semester = models.ForeignKey(Semester, related_name='schedules', on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s- %s (%s)' % (self.bus.bus_number, self.bus.bus_name, self.trip_direction, self.semester.__str__())

    class Meta:
        ordering = ['bus', 'trip_direction', 'semester']
        constraints = [
            UniqueConstraint(fields=['semester', 'bus', 'trip_direction'], name='unique_service')
        ]


class Enrollment(models.Model):
    enroll_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='enrollments', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='enrollments', on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.service, self.user)

    class Meta:
        ordering = ['service', 'user']
        constraints = [
            UniqueConstraint(fields=['service', 'user'], name='unique_enrollment')
        ]



