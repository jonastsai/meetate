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
#from greencoffee.models import GreenCoffees
#from roastlogs.models import RoastTimelogs, Roastlogs
from greencoffees.models import *
from roastlogs.models import *


class Orders(models.Model):
    create_at = models.DateField(blank=True, null=True)
    output_at = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User)
    status = models.IntegerField()
    running_total = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'orders'
        app_label = 'orders'
        verbose_name_plural = 'Orders'

    def __unicode__(self):
            return u'%s, %s' % (self.create_at, self.user.username)

class Products(models.Model):
    green_coffee = models.ForeignKey(GreenCoffees)
    list_price = models.IntegerField()
    weight = models.IntegerField()
    create_at = models.DateField()
    status = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'products'
        app_label = 'orders'
        verbose_name_plural = 'Products'

    def __unicode__(self):
            return u'%s, %s, %s' % (self.create_at, self.green_coffee.name, self.green_coffee.processStr(self.green_coffee.process))

class SellingItems(models.Model):
    order = models.ForeignKey(Orders)
    roastlog = models.ForeignKey("roastlogs.Roastlogs", blank=True, null=True)
    selling_price = models.IntegerField()
    product = models.ForeignKey(Products)

    class Meta:
        #managed = False
        db_table = 'selling_items'
        app_label = 'orders'
        verbose_name_plural = 'Selling Items'

