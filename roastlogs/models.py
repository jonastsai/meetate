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

import os
from django.db import models
from django.contrib.auth.models import User
#from orders.models import Orders, Products, SellingItems
from orders.models import *
from greencoffees.models import *

class RoastTimelogs(models.Model):
    roastlog = models.ForeignKey('Roastlogs', blank=True, null=True)
    second = models.IntegerField()
    bt = models.IntegerField()
    temp1 = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    fan_level = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'roast_timelogs'
        app_label = 'roastlogs'
        verbose_name_plural = "Roast Time Logs"


class Roastlogs(models.Model):
    cust_index = models.CharField(max_length=20, blank=True, null=True)
    #green_coffee = models.ForeignKey(GreenCoffees, blank=True, null=True)
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
    random_str = models.CharField(max_length=10, blank=True, null=True)
    time_log_str = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'roastlogs'
        app_label = 'roastlogs'
        verbose_name_plural = "Roast Logs"

    def __unicode__(self):
        return u'%s, %s' % (self.cust_index, self.start_time)

    def duration(self):
        if self.start_time != None and self.end_time != None:
            return self.end_time - self.start_time
        return 'n/a'

    def lost_percent(self):
        if self.start_weight != None and self.end_weight != None:
            lost = self.start_weight - self.end_weight
            return '{percent:.1%}'.format(percent=float(lost)/float(self.start_weight))
        return 'n/a'

    def green_coffee(self):
        try:
            sale = SellingItems.objects.get(roastlog=self)
            if sale != None:
                return sale.product.green_coffee
        except Exception:
            return "No such coffee"
        return "You should not see this"

    def curve_image_url(self):
        # TODO We should get the urlbase according to user's property
        urlbase = os.environ.get("MEETATE_URL_BASE", '')
        fileName = self.start_time.strftime('%Y%m%d_%H%M%S') + "_" + self.random_str + ".png"
        return urlbase + fileName

    def curve_image(self):
        #return '<img src="http://nviki.qiniudn.com/80909_medium.jpg"/>'
        return '<img src="%s" height="320" width="480"/>' % (self.curve_image_url())
    curve_image.allow_tags = True

