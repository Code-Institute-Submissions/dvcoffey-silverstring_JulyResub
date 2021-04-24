from django.contrib import admin
from .models import Showcase

# Register your models here.


class ShowcaseAdmin(admin.ModelAdmin):
    list_display = (
        'start_date',
        'start_time',
        'location',
        'entry_fee',
    )
