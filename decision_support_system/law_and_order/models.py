from django.db import models


class Crime(models.Model):
    type = models.CharField(max_length=255)
    nearest_police_station_name = models.CharField(max_length=255)
    nearest_police_station_distance = models.IntegerField()
    nearest_hospital_name = models.CharField(max_length=255)
    police_arrangement = models.TextField(blank=True, null=True)
    medical_arrangement = models.TextField(blank=True, null=True)
    forensics_arrangement = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crime'


class Epidemic(models.Model):
    type = models.CharField(max_length=255)
    people_died = models.IntegerField(blank=True, null=True)
    people_cured = models.IntegerField(blank=True, null=True)
    medical_arrangement = models.TextField(blank=True, null=True)
    police_arrangement = models.TextField(blank=True, null=True)
    food_arrangement = models.TextField(blank=True, null=True)
    government_cost = models.IntegerField(blank=True, null=True)
    camps = models.CharField(max_length=255, blank=True, null=True)
    evacuation_mode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'epidemic'


class NaturalCalamities(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    people_affected = models.IntegerField(blank=True, null=True)
    medical_arrangement = models.TextField(blank=True, null=True)
    police_arrangement = models.TextField(blank=True, null=True)
    food_arrangement = models.TextField(blank=True, null=True)
    government_cost = models.IntegerField(blank=True, null=True)
    camps = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'natural_calamities'


class PublicGathering(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField()
    venue = models.CharField(max_length=255)
    area = models.CharField(max_length=255, blank=True, null=True)
    political_leader = models.CharField(max_length=255)
    social_leader = models.CharField(max_length=255, blank=True, null=True)
    religious_leader = models.CharField(max_length=255, blank=True, null=True)
    government_official = models.CharField(max_length=255, blank=True, null=True)
    police_personnel_deployed = models.IntegerField(blank=True, null=True)
    ambulances_deployed = models.IntegerField(blank=True, null=True)
    fire_fighters_deployed = models.IntegerField(blank=True, null=True)
    vehicles = models.IntegerField(blank=True, null=True)
    participants = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_gathering'


class Rally(models.Model):
    name = models.CharField(max_length=255)
    political_leader = models.CharField(max_length=255, blank=True, null=True)
    social_leader = models.CharField(max_length=255, blank=True, null=True)
    religious_leader = models.CharField(max_length=255, blank=True, null=True)
    government_official = models.CharField(max_length=255, blank=True, null=True)
    route = models.CharField(max_length=255)
    critical_level = models.IntegerField()
    participants = models.IntegerField(blank=True, null=True)
    police_personnel_deployed = models.IntegerField(blank=True, null=True)
    ambulances_deployed = models.IntegerField(blank=True, null=True)
    fire_fighters_deployed = models.IntegerField(blank=True, null=True)
    vehicles = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'rally'

