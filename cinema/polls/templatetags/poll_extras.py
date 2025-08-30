from django import template
from jalali_date import datetime2jalali, date2jalali

register = template.Library()

@register.filter(name='show_jalali_data')
def show_jalali_data(value):
    return date2jalali(value)
    
@register.filter(name='show_jalali_time')
def show_jalali_time(value):
    return datetime2jalali(value)
        
        

