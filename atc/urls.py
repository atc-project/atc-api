from rest_framework.routers import DefaultRouter
from django.urls import path, include
from atc import viewsets



router = DefaultRouter()
router.register(r'category', viewsets.CategoryViewSet)
router.register(r'platform', viewsets.PlatformViewSet)
router.register(r'logtype', viewsets.LogTypeViewSet)
router.register(r'channel', viewsets.ChannelViewSet)
router.register(r'provider', viewsets.ProviderViewSet)
router.register(r'volume', viewsets.VolumeViewSet)
router.register(r'logfield', viewsets.LogFieldViewSet)
router.register(r'stage', viewsets.StageViewSet)
router.register(r'eventid', viewsets.EventIdViewSet)
router.register(r'tag', viewsets.TagViewSet)
router.register(r'reference', viewsets.ReferenceViewSet)
router.register(r'loggingpolicy', viewsets.LoggingPolicyViewSet)
router.register(r'dataneeded', viewsets.DataNeededViewSet)
router.register(r'enrichment', viewsets.EnrichmentViewSet)
router.register(r'responseaction', viewsets.ResponseActionViewSet)
router.register(r'responseplaybook', viewsets.ResponsePlaybookViewSet)
router.register(r'detectionrule', viewsets.DetectionRuleViewSet)









urlpatterns = [
    path('', include(router.urls)),
]