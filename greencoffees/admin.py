# -*- coding: utf-8 -*-
from django.contrib import admin
from models import GreenCoffees, Vendors
class NotEmptyFilter(admin.SimpleListFilter):
    title = 'Been Available'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'qty_now'

    def lookups(self, request, model_admin):
        return (
            (None, 'Non-Empty'),
            ('empty', 'Empty'),
            ('all', 'All'),
        )

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }
    def queryset(self, request, queryset):
        if self.value() == 'empty':
            return queryset.filter(qty_now = 0)
        if self.value() == 'all':
            return queryset.filter()
        else:
            return queryset.filter(qty_now__gt=0)

class GreenCoffeesAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "process", "price", "qty_in", "qty_now", "vendor", "create_at")
    radio_fields = {"process": admin.VERTICAL}
    list_per_page = int(20)
    list_filter = (NotEmptyFilter, 'process', 'vendor')
'''
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "process":
            kwargs['choices'] = (
                ('0', '100'),
                ('1', '101'),
                ('2', '102'),
            )
        return super(GreenCoffeesAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)
'''
class VendorsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_per_page = int(10)

# Register your models here.
admin.site.register(GreenCoffees, GreenCoffeesAdmin)
admin.site.register(Vendors, VendorsAdmin)
