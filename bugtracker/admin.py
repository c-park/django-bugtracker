from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Ticket

class TicketAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'priority', 'status']
    list_display_links = ['title']
    
    search_fields = ['title', 'description']
    list_filter = ['timestamp', 'status', 'priority']
    
    date_hierarchy = 'timestamp'
    
    def close_tickets(self, request, queryset):
        tickets = queryset.update(status=1)
        if tickets == 1:
            msg = _('A ticket has been marked as closed')
        else:
            msg = _("%s Ticket's are marked as closed") % tickets
        self.message_user(request, msg)
    close_tickets.short_description = _("Close Ticket's")

admin.site.register(Ticket, TicketAdmin)