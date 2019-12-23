from django.db import models


class EventTable(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    date_of_event = models.DateTimeField()
    comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_table'


class Rally(models.Model):
    political_leader = models.CharField(max_length=255)
    protest = models.TextField()
    religion = models.CharField(max_length=255)
    date_time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rally'


class Riots(models.Model):
    regional_party = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    community_caste = models.CharField(max_length=255)
    date_time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riots'


class VipLeader(models.Model):
    pp_leader = models.CharField(max_length=255)
    religion_leader = models.CharField(max_length=255)
    administrative_leader = models.CharField(max_length=255)
    famous_personality = models.CharField(max_length=255)
    date_time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vip_leader'


class CriticalRoute(models.Model):
    crime = models.TextField()
    congestion = models.TextField()
    date_time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'critical_route'
