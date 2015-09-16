from django.contrib import admin
from models import Roastlogs, RoastTimelogs
from customlogs import *

class RoastlogsAdmin(admin.ModelAdmin):
    list_display = ("cust_index", "green_coffee", "start_time", "duration", "start_weight", "end_weight", "lost_percent", "order_of_day", "curve_image")
    list_per_page = int(10)
    change_form = RoastlogsForm

    '''
    fieldsets = (
        (None, {
            'fields': ('cust_index', 'green_coffee', 'start_time', 'duration', 'lost_percent'),
        }),
    )
    '''

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            kwargs['form'] = self.change_form
            #kwargs['duration'] = obj.duration()
            fields = ['cust_index', 'green_coffee', 'curve_image', 'start_time', 'duration', 'start_weight', 'end_weight', 'lost_percent', 'env_temp', 'env_humi']
            #self.fields = ['cust_index', 'green_coffee', 'start_time', 'duration', 'lost_percent']
        else:
            self.fields = ['cust_index', 'green_coffee', 'start_time']
        return super(RoastlogsAdmin, self).get_form(request, obj, **kwargs)

# Register your models here.
admin.site.register(Roastlogs, RoastlogsAdmin)
#admin.site.register(RoastTimelogs)
