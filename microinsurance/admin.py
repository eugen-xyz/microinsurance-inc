from django.contrib import admin
from .models import Underwriter, Branche, Insurance, Applicant


#$admin.site.unregister(Group)
admin.site.register(Underwriter)
admin.site.register(Branche)
admin.site.register(Insurance)
admin.site.register(Applicant)
