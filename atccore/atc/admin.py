from django.contrib import admin
from atc.models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class PlatformAdmin(admin.ModelAdmin):
    pass


class LogTypeAdmin(admin.ModelAdmin):
    pass


class ChannelAdmin(admin.ModelAdmin):
    pass


class ProviderAdmin(admin.ModelAdmin):
    pass


class VolumeAdmin(admin.ModelAdmin):
    pass


class LogFieldAdmin(admin.ModelAdmin):
    pass


class StageAdmin(admin.ModelAdmin):
    pass


class EventIDAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class ReferencesAdmin(admin.ModelAdmin):
    pass


class LoggingPolicyAdmin(admin.ModelAdmin):
    pass


class DataNeededAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


class EnrichmentAdmin(admin.ModelAdmin):
    pass


class ResponseActionAdmin(admin.ModelAdmin):
    pass


class ResponsePlaybookAdmin(admin.ModelAdmin):
    pass


class DetectionRuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(LogType, LogTypeAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(LogField, LogFieldAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(EventID, EventIDAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(References, ReferencesAdmin)
admin.site.register(LoggingPolicy, LoggingPolicyAdmin)
admin.site.register(DataNeeded, DataNeededAdmin)
admin.site.register(Enrichment, EnrichmentAdmin)
admin.site.register(ResponseAction, ResponseActionAdmin)
admin.site.register(ResponsePlaybook, ResponsePlaybookAdmin)
admin.site.register(DetectionRule, DetectionRuleAdmin)
