from rest_framework import viewsets, permissions
import atc.models as models
import atc.serializers as serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.AllowAny,)


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    permission_classes = (permissions.AllowAny,)


class LogTypeViewSet(viewsets.ModelViewSet):
    queryset = models.LogType.objects.all()
    serializer_class = serializers.LogTypeSerializer
    permission_classes = (permissions.AllowAny,)


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
    permission_classes = (permissions.AllowAny,)


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer
    permission_classes = (permissions.AllowAny,)


class VolumeViewSet(viewsets.ModelViewSet):
    queryset = models.Volume.objects.all()
    serializer_class = serializers.VolumeSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(VolumeViewSet, self).retrieve(request, *self.args, **self.kwargs)
        return super(VolumeViewSet, self).create(request, *args, **kwargs)



class LogFieldViewSet(viewsets.ModelViewSet):
    queryset = models.LogField.objects.all()
    serializer_class = serializers.LogFieldSerializer
    permission_classes = (permissions.AllowAny,)


class StageViewSet(viewsets.ModelViewSet):
    queryset = models.Stage.objects.all()
    serializer_class = serializers.StageSerializer
    permission_classes = (permissions.AllowAny,)


class EventIdViewSet(viewsets.ModelViewSet):
    queryset = models.EventID.objects.all()
    serializer_class = serializers.EventIDSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        data = request.data
        event_id = data['id']
        self.kwargs['id'] = event_id
        if self.queryset.filter(id=event_id):
            return super(EventIdViewSet, self).retrieve(request, *self.args, **self.kwargs)
        return super(EventIdViewSet, self).create(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (permissions.AllowAny,)


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = models.Reference.objects.all()
    serializer_class = serializers.ReferenceSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        url = data['url']
        if self.queryset.filter(url=url):
            obj = self.queryset.filter(url=url).first()
            self.kwargs['pk'] = obj.id
            return super(ReferenceViewSet, self).retrieve(request, *self.args, **self.kwargs)
        return super(ReferenceViewSet, self).create(request, *args, **kwargs)



class LoggingPolicyViewSet(viewsets.ModelViewSet):
    queryset = models.LoggingPolicy.objects.all()
    serializer_class = serializers.LoggingPolicySerializer
    permission_classes = (permissions.AllowAny,)



class DataNeededViewSet(viewsets.ModelViewSet):
    queryset = models.DataNeeded.objects.all()
    serializer_class = serializers.DataNeededSerializer
    permission_classes = (permissions.AllowAny,)


class EnrichmentViewSet(viewsets.ModelViewSet):
    queryset = models.Enrichment.objects.all()
    serializer_class = serializers.EnrichmentSerializer
    permission_classes = (permissions.AllowAny,)


class ResponseActionViewSet(viewsets.ModelViewSet):
    queryset = models.ResponseAction.objects.all()
    serializer_class = serializers.ResponseActionSerializer
    permission_classes = (permissions.AllowAny,)


class ResponsePlaybookViewSet(viewsets.ModelViewSet):
    queryset = models.ResponsePlaybook.objects.all()
    serializer_class = serializers.ResponsePlaybookSerializer
    permission_classes = (permissions.AllowAny,)


class DetectionRuleViewSet(viewsets.ModelViewSet):
    queryset = models.DetectionRule.objects.all()
    serializer_class = serializers.DetectionRuleSerializer
    permission_classes = (permissions.AllowAny,)


