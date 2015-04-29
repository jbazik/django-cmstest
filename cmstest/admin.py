from django.contrib.admin import ModelAdmin
from cms.admin.placeholderadmin import PlaceholderAdminMixin


class CMSTestAdmin(PlaceholderAdminMixin, ModelAdmin):
    pass
