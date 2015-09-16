from django.forms import ModelForm
from django.forms import widgets
from django import template
from django import forms
from string import Template
from roastlogs.models import *
from django.forms.widgets import FileInput
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        html = Template("""<img src="$link" height="600" width="800"/>""")
        return mark_safe(html.substitute(link=value))


class RoastlogsForm(forms.ModelForm):

    green_coffee = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))
    duration = forms.CharField()
    lost_percent = forms.CharField()
    curve_image = forms.ImageField(widget=PictureWidget)

    def __init__(self, *args, **kwargs):

        instance = kwargs.get('instance')
        if instance:
            self.base_fields['duration'].initial = instance.duration()
            self.base_fields['lost_percent'].initial = instance.lost_percent()
            self.base_fields['green_coffee'].initial = instance.green_coffee()
            self.base_fields['curve_image'].initial = instance.curve_image_url()
        self.base_fields['duration'].widget.attrs['readonly'] = True
        self.base_fields['lost_percent'].widget.attrs['readonly'] = True
        self.base_fields['green_coffee'].widget.attrs['readonly'] = True
        forms.ModelForm.__init__(self, *args, **kwargs)

    class Meta:
        model = Roastlogs
        fields = ['cust_index', 'green_coffee', 'curve_image', 'start_time',
                'duration', 'start_weight', 'end_weight', 'lost_percent',
                'env_temp', 'env_humi', 'order_of_day', 'status']
'''
    def save(self, commit=True):
        extra_field = self.cleaned_data.get('extra_field', None)
        # ...do something with extra_field here...
        return super(YourModelForm, self).save(commit=commit)
'''
