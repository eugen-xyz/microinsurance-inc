from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Underwriter, Branch, Product, Applicant


admin.site.unregister(Group)
admin.site.register(Underwriter)
admin.site.register(Branch)
admin.site.register(Product)
admin.site.register(Applicant)
