from django.contrib import admin
from reminder.models import Event, Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    list_filter = ('send_type',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('send_type',)
