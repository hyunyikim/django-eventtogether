# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Events(models.Model):
    eid = models.CharField(primary_key=True, max_length=15)
    ename = models.CharField(max_length=100, blank=True, null=True)
    econtent = models.TextField(blank=True, null=True)
    ecreater = models.CharField(max_length=40, blank=True, null=True)
    eloc = models.CharField(max_length=40, blank=True, null=True)
    estartdt = models.DateField(blank=True, null=True)
    estarttm = models.TimeField(blank=True, null=True)
    eenddt = models.DateField(blank=True, null=True)
    eendtm = models.TimeField(blank=True, null=True)
    eprice = models.IntegerField(blank=True, null=True)
    emaxattendee = models.IntegerField(blank=True, null=True)
    eculattendee = models.IntegerField(blank=True, null=True)
    eimage = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'
