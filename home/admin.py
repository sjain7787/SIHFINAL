from django.contrib import admin
from home.models import Export1, Feedback, Import1, Immigrations, Account,BOEHome,BOEwarehousing,BOEExHome,Portoperations,Portaudit
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AccountInline(admin.StackedInline):
    model = Account
    can_delete: False
    verbose_name_plural = 'Accounts'




class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInline,)


admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(Feedback)
admin.site.register(Import1)
admin.site.register(Export1)
admin.site.register(Immigrations)
admin.site.register(BOEHome)
admin.site.register(BOEwarehousing)
admin.site.register(BOEExHome)
admin.site.register(Portoperations)
admin.site.register(Portaudit)