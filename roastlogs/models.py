# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from order.models import Orders, Products, SellingItems
from greencoffees.models import *

class RoastTimelogs(models.Model):
    roastlog = models.ForeignKey('Roastlogs')
    second = models.IntegerField()
    bt = models.IntegerField()
    temp1 = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    fan_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roast_timelogs'
        app_label = 'roastlogs'
        verbose_name_plural = "Roast Time Logs"


class Roastlogs(models.Model):
    cust_index = models.CharField(max_length=20, blank=True, null=True)
    green_coffee = models.ForeignKey(GreenCoffees)
    comment = models.CharField(max_length=200, blank=True, null=True)
    taste = models.CharField(max_length=200, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_weight = models.IntegerField(blank=True, null=True)
    end_weight = models.IntegerField(blank=True, null=True)
    env_temp = models.IntegerField(blank=True, null=True)
    env_humi = models.IntegerField(blank=True, null=True)
    roastor_dev_id = models.CharField(max_length=10, blank=True, null=True)
    roastor = models.ForeignKey(User, blank=True, null=True)
    order_of_day = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    curve_file = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roastlogs'
        app_label = 'roastlogs'
        verbose_name_plural = "Roast Logs"

