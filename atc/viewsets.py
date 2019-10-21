from rest_framework import viewsets, permissions
import atc.models as models
import atc.serializers as serializers
# from rest_framework.decorators import action


class ReadOnlyPermissions(permissions.BasePermission):
    """
    Read Only permission class
    """
    message = "You are not allowed to directly interact with this entity"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(CategoryViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(CategoryViewSet, self).create(
            request, *args, **kwargs
        )


class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(PlatformViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(PlatformViewSet, self).create(
            request, *args, **kwargs
        )


class LogTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.LogType.objects.all()
    serializer_class = serializers.LogTypeSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(LogTypeViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(LogTypeViewSet, self).create(
            request, *args, **kwargs
        )


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(ChannelViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(ChannelViewSet, self).create(
            request, *args, **kwargs
        )


class ProviderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(ProviderViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(ProviderViewSet, self).create(
            request, *args, **kwargs
        )


class VolumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Volume.objects.all()
    serializer_class = serializers.VolumeSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(VolumeViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(VolumeViewSet, self).create(
            request, *args, **kwargs
        )


class LogFieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.LogField.objects.all()
    serializer_class = serializers.LogFieldSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(LogFieldViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(LogFieldViewSet, self).create(
            request, *args, **kwargs
        )


class StageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Stage.objects.all()
    serializer_class = serializers.StageSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(StageViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(StageViewSet, self).create(
            request, *args, **kwargs
        )


class EventIdViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.EventID.objects.all()
    serializer_class = serializers.EventIDSerializer
    permission_classes = (ReadOnlyPermissions,)
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        data = request.data
        event_id = data['id']
        self.kwargs['id'] = event_id
        if self.queryset.filter(id=event_id):
            return super(EventIdViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(EventIdViewSet, self).create(
            request, *args, **kwargs
        )


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data['name']
        if self.queryset.filter(name=name):
            obj = self.queryset.filter(name=name).first()
            self.kwargs['pk'] = obj.id
            return super(TagViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(TagViewSet, self).create(
            request, *args, **kwargs
        )


class ReferencesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.References.objects.all()
    serializer_class = serializers.ReferencesSerializer
    permission_classes = (ReadOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        data = request.data
        url = data['url']
        if self.queryset.filter(url=url):
            obj = self.queryset.filter(url=url).first()
            self.kwargs['pk'] = obj.id
            return super(ReferencesViewSet, self).retrieve(
                request, *self.args, **self.kwargs
            )
        return super(ReferencesViewSet, self).create(
            request, *args, **kwargs
        )

# ################################################################ #
# ##################### Strict ATC ViewSets ###################### #
# ################################################################ #


class LoggingPolicyViewSet(viewsets.ModelViewSet):
    queryset = models.LoggingPolicy.objects.all()
    serializer_class = serializers.LoggingPolicySerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        title = data['title']
        if self.queryset.filter(title=title):
            obj = self.queryset.filter(title=title).first()
            self.kwargs['pk'] = obj.id
            return super(LoggingPolicyViewSet, self).update(
                request, *self.args, **self.kwargs
            )
        return super(LoggingPolicyViewSet, self).create(
            request, *args, **kwargs
        )


class DataNeededViewSet(viewsets.ModelViewSet):
    queryset = models.DataNeeded.objects.all()
    serializer_class = serializers.DataNeededSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        title = data['title']
        if self.queryset.filter(title=title):
            obj = self.queryset.filter(title=title).first()
            self.kwargs['pk'] = obj.id
            return super(DataNeededViewSet, self).update(
                request, *self.args, **self.kwargs
            )
        return super(DataNeededViewSet, self).create(
            request, *args, **kwargs
        )


class EnrichmentViewSet(viewsets.ModelViewSet):
    queryset = models.Enrichment.objects.all()
    serializer_class = serializers.EnrichmentSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        title = data['title']
        if self.queryset.filter(title=title):
            obj = self.queryset.filter(title=title).first()
            self.kwargs['pk'] = obj.id
            return super(EnrichmentViewSet, self).update(
                request, *self.args, **self.kwargs
            )
        return super(EnrichmentViewSet, self).create(
            request, *args, **kwargs
        )


class ResponseActionViewSet(viewsets.ModelViewSet):
    queryset = models.ResponseAction.objects.all()
    serializer_class = serializers.ResponseActionSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        title = data['title']
        if self.queryset.filter(title=title):
            obj = self.queryset.filter(title=title).first()
            self.kwargs['pk'] = obj.id
            return super(ResponseActionViewSet, self).update(
                request, *self.args, **self.kwargs
            )
        return super(ResponseActionViewSet, self).create(
            request, *args, **kwargs
        )


class ResponsePlaybookViewSet(viewsets.ModelViewSet):
    queryset = models.ResponsePlaybook.objects.all()
    serializer_class = serializers.ResponsePlaybookSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        title = data['title']
        if self.queryset.filter(title=title):
            obj = self.queryset.filter(title=title).first()
            self.kwargs['pk'] = obj.id
            return super(ResponsePlaybookViewSet, self).update(
                request, *self.args, **self.kwargs
            )
        return super(ResponsePlaybookViewSet, self).create(
            request, *args, **kwargs
        )


class DetectionRuleViewSet(viewsets.ModelViewSet):
    queryset = models.DetectionRule.objects.all()
    serializer_class = serializers.DetectionRuleSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        title = data['title']
        if self.queryset.filter(title=title):
            obj = self.queryset.filter(title=title).first()
            self.kwargs['pk'] = obj.id
            return super(DetectionRuleViewSet, self).update(
                request, *self.args, **self.kwargs
            )
        return super(DetectionRuleViewSet, self).create(
            request, *args, **kwargs
        )
