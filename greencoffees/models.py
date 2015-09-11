# -*- coding: utf-8 -*-
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
#from roastlogs.models import RoastTimelogs, Roastlogs
#from order.models import Orders, Products, SellingItems
#from roastlogs.models import *
#from orders.models import *

class Vendors(models.Model):
    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=30, blank=True, null=True)
    tel = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'vendors'
        app_label = 'greencoffees'
        verbose_name_plural = "Green Coffee Vendor"

    def __unicode__(self):
        return u'%s' % (self.name)

class GreenCoffees(models.Model):
    PROCESS_CHOICES = ((0, '水洗'), (1, '日曬'), (2, '蜜處理'))
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30, blank=True, null=True)
    manor = models.CharField(max_length=30, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    process = models.IntegerField(choices=PROCESS_CHOICES)
    price = models.IntegerField()
    qty_in = models.IntegerField()
    qty_now = models.IntegerField(blank=True, null=True)
    defect = models.IntegerField(blank=True, null=True)
    vendor = models.ForeignKey(Vendors)
    #seller = models.CharField(max_length=30, blank=True, null=True)
    official_taste = models.CharField(max_length=100, blank=True, null=True)
    official_desc = models.TextField(blank=True, null=True)
    self_taste = models.CharField(max_length=60, blank=True, null=True)
    create_at = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'green_coffees'
        app_label = 'greencoffees'
        verbose_name_plural = "Green Coffees"

    def __unicode__(self):
        return u'%s %s, %s' % (self.country, self.name, self.processStr(self.process))

    def processStr(self, index):
        strs = ['水洗', '日曬', '蜜處理']
        return strs[index]


