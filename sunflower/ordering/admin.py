from django.contrib import admin
from ordering.models import Order
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("email", "picture", "reviewed", "finished", "created_at", "modified_at", "short_notes")
    search_fields= ("email", "picture", "notes")
    list_filter = ("reviewed", "finished", "email")
    
    def short_notes(self, order):
        return order.notes[:20] + ('...' if len(order.notes)>20 else "")