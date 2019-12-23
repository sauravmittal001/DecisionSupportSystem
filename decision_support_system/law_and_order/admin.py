from django.contrib import admin
from .models import EventTable, Rally, Riots, VipLeader, CriticalRoute

# Register your models here.

admin.site.register(EventTable)
admin.site.register(Rally)
admin.site.register(CriticalRoute)
admin.site.register(Riots)
admin.site.register(VipLeader)
