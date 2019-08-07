from rest_framework import viewsets, permissions
import atc.models as models
import atc.serializers as serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LogTypeViewSet(viewsets.ModelViewSet):
    queryset = models.LogType.objects.all()
    serializer_class = serializers.LogTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer
    permission_classes = (permissions.IsAuthenticated,)


class VolumeViewSet(viewsets.ModelViewSet):
    queryset = models.Volume.objects.all()
    serializer_class = serializers.VolumeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LogFieldViewSet(viewsets.ModelViewSet):
    queryset = models.LogField.objects.all()
    serializer_class = serializers.LogFieldSerializer
    permission_classes = (permissions.IsAuthenticated,)


class StageViewSet(viewsets.ModelViewSet):
    queryset = models.Stage.objects.all()
    serializer_class = serializers.StageSerializer
    permission_classes = (permissions.IsAuthenticated,)


class EventIdViewSet(viewsets.ModelViewSet):
    queryset = models.EventID.objects.all()
    serializer_class = serializers.EventIdSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class LoggingPolicyViewSet(viewsets.ModelViewSet):
    queryset = models.LoggingPolicy.objects.all()
    serializer_class = serializers.LoggingPolicySerializer
    permission_classes = (permissions.IsAuthenticated,)


class DataNeededViewSet(viewsets.ModelViewSet):
    queryset = models.DataNeeded.objects.all()
    serializer_class = serializers.DataNeededSerializer
    permission_classes = (permissions.IsAuthenticated,)


class EnrichmentViewSet(viewsets.ModelViewSet):
    queryset = models.Enrichment.objects.all()
    serializer_class = serializers.EnrichmentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ResponseActionViewSet(viewsets.ModelViewSet):
    queryset = models.ResponseAction.objects.all()
    serializer_class = serializers.ResponseActionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ResponsePlaybookViewSet(viewsets.ModelViewSet):
    queryset = models.ResponsePlaybook.objects.all()
    serializer_class = serializers.ResponsePlaybookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DetectionRuleViewSet(viewsets.ModelViewSet):
    queryset = models.DetectionRule.objects.all()
    serializer_class = serializers.DetectionRuleSerializer
    permission_classes = (permissions.IsAuthenticated,)


