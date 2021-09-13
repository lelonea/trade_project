from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from user.models import User


class UserAdmin(admin.ModelAdmin):
    actions = ['create_password']
    list_display = ('email', 'is_active')
    fields = [('email', 'is_active')]
    list_filter = ['is_active', 'email']
    search_fields = ['email']

    def create_password(self, request, queryset):
        user_qs = User.objects.filter(pk__in=queryset.values_list('pk', flat=True))

        for user in user_qs:
            user.create_password_send_email()
        self.message_user(request, _('{} create password email(s) sent').format(user_qs.count()))

    create_password.short_description = "Send email for user to create a password"


admin.site.site_header = 'Trading platform system'
admin.site.index_title = 'Trading platform system'
admin.site.site_title = 'Trading platform system'

admin.site.register(User, UserAdmin)
