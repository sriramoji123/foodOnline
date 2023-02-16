from django.contrib import admin
from vendor.models import Vendor
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ('user','vendor_name','user_profile','is_approved','created_at')
    list_display_links= ('user','vendor_name')
    #Here list_display_links indicates that it is a link on clicking it redirects to the form
    
    #to make the password not editable
    


admin.site.register(Vendor,VendorAdmin)