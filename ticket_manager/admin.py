from django.contrib import admin
from ticket_manager.models import User, Ticket, Site
# Register your models here.
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Site)
