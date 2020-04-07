import atc.models as models
import atc.serializers as serializers
import json
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
# from rest_framework.decorators import action


class ReadOnlyPermissions(permissions.BasePermission):
    """
    Read Only permission class
    """

    message = "You are not allowed to directly interact with this entity"

    def has_object_permission(self, request, view, obj):
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


class LoggingPolicyFilter(filters.FilterSet):

    title_contains = filters.CharFilter(
        field_name='title', lookup_expr='icontains',
        distinct=True
    )
    title_exact = filters.CharFilter(
        field_name='title', lookup_expr='iexact',
        distinct=True
    )
    eventID_exact = filters.CharFilter(
        field_name='eventID', lookup_expr='exact',
        distinct=True
    )
    volume_exact = filters.CharFilter(
        field_name='volume', lookup_expr='name__iexact',
        distinct=True
    )

    class Meta:
        model = models.LoggingPolicy
        fields = []


class LoggingPolicyViewSet(viewsets.ModelViewSet):
    queryset = models.LoggingPolicy.objects.all()
    serializer_class = serializers.LoggingPolicySerializer
    permission_classes = (permissions.AllowAny,)
    filterset_class = LoggingPolicyFilter

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


class DataNeededFilter(filters.FilterSet):

    loggingpolicy_contains = filters.CharFilter(
        field_name='loggingpolicy', lookup_expr='title__icontains',
        distinct=True
    )
    title_contains = filters.CharFilter(
        field_name='title', lookup_expr='icontains',
        distinct=True
    )
    category_contains = filters.CharFilter(
        field_name='category', lookup_expr='name__icontains',
        distinct=True
    )
    channel_contains = filters.CharFilter(
        field_name='channel', lookup_expr='name__icontains',
        distinct=True
    )
    platform_contains = filters.CharFilter(
        field_name='platform', lookup_expr='name__icontains',
        distinct=True
    )
    provider_contains = filters.CharFilter(
        field_name='provider', lookup_expr='name__icontains',
        distinct=True
    )
    fields_contains = filters.CharFilter(
        field_name='fields', lookup_expr='name__icontains',
        distinct=True
    )

    loggingpolicy_exact = filters.CharFilter(
        field_name='loggingpolicy', lookup_expr='title__iexact',
        distinct=True
    )
    title_exact = filters.CharFilter(
        field_name='title', lookup_expr='iexact',
        distinct=True
    )
    category_exact = filters.CharFilter(
        field_name='category', lookup_expr='name__iexact',
        distinct=True
    )
    channel_exact = filters.CharFilter(
        field_name='channel', lookup_expr='name__iexact',
        distinct=True
    )
    platform_exact = filters.CharFilter(
        field_name='platform', lookup_expr='name__iexact',
        distinct=True
    )
    provider_exact = filters.CharFilter(
        field_name='provider', lookup_expr='name__iexact',
        distinct=True
    )
    fields_exact = filters.CharFilter(
        field_name='fields', lookup_expr='name__iexact',
        distinct=True
    )
    eventid_exact = filters.CharFilter(
        field_name='eventID', lookup_expr='id__iexact',
        distinct=True
    )

    class Meta:
        model = models.DataNeeded
        fields = []


class DataNeededViewSet(viewsets.ModelViewSet):
    queryset = models.DataNeeded.objects.all()
    serializer_class = serializers.DataNeededSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_class = DataNeededFilter

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


class EnrichmentFilter(filters.FilterSet):

    title_contains = filters.CharFilter(
        field_name='title', lookup_expr='icontains',
        distinct=True
    )
    data_needed_contains = filters.CharFilter(
        field_name='data_needed', lookup_expr='title__icontains',
        distinct=True
    )
    data_to_enrich_contains = filters.CharFilter(
        field_name='data_to_enrich', lookup_expr='title__icontains',
        distinct=True
    )
    requirements_contains = filters.CharFilter(
        field_name='requirements', lookup_expr='title__icontains',
        distinct=True
    )
    new_fields_contains = filters.CharFilter(
        field_name='new_fields', lookup_expr='name__icontains',
        distinct=True
    )

    title_exact = filters.CharFilter(
        field_name='title', lookup_expr='iexact',
        distinct=True
    )
    data_needed_exact = filters.CharFilter(
        field_name='data_needed', lookup_expr='title__iexact',
        distinct=True
    )
    data_to_enrich_exact = filters.CharFilter(
        field_name='data_to_enrich', lookup_expr='title__iexact',
        distinct=True
    )
    requirements_exact = filters.CharFilter(
        field_name='requirements', lookup_expr='title__iexact',
        distinct=True
    )
    new_fields_exact = filters.CharFilter(
        field_name='new_fields', lookup_expr='name__iexact',
        distinct=True
    )

    class Meta:
        model = models.Enrichment
        fields = []


class EnrichmentViewSet(viewsets.ModelViewSet):
    queryset = models.Enrichment.objects.all()
    serializer_class = serializers.EnrichmentSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_class = EnrichmentFilter

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


class DetectionRuleFilter(filters.FilterSet):

    title_contains = filters.CharFilter(
        field_name='title', lookup_expr='icontains',
        distinct=True
    )

    description_contains = filters.CharFilter(
        field_name='description', lookup_expr='icontains',
        distinct=True
    )

    tag_contains = filters.CharFilter(
        field_name='tag', lookup_expr='name__icontains',
        distinct=True
    )

    severity_contains = filters.CharFilter(
        field_name='severity', lookup_expr='icontains',
        distinct=True
    )

    status_contains = filters.CharFilter(
        field_name='status', lookup_expr='icontains',
        distinct=True
    )

    author_contains = filters.CharFilter(
        field_name='author', lookup_expr='icontains',
        distinct=True
    )

    title_exact = filters.CharFilter(
        field_name='title', lookup_expr='iexact',
        distinct=True
    )

    description_exact = filters.CharFilter(
        field_name='description', lookup_expr='iexact',
        distinct=True
    )

    tag_exact = filters.CharFilter(
        field_name='tag', lookup_expr='name__iexact',
        distinct=True
    )

    severity_exact = filters.CharFilter(
        field_name='severity', lookup_expr='iexact',
        distinct=True
    )

    status_exact = filters.CharFilter(
        field_name='status', lookup_expr='iexact',
        distinct=True
    )

    author_exact = filters.CharFilter(
        field_name='author', lookup_expr='iexact',
        distinct=True
    )

    dataneeded_isnull = filters.BooleanFilter(
        field_name='data_needed', lookup_expr='isnull',
        distinct=True, label="Data Needed is NULL"
    )

    rawrule_contains = filters.CharFilter(
        field_name='raw_rule', lookup_expr='icontains',
        distinct=True
    )


class DetectionRuleViewSet(viewsets.ModelViewSet):
    queryset = models.DetectionRule.objects.all()
    serializer_class = serializers.DetectionRuleSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_class = DetectionRuleFilter

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            title = data['raw_rule'][0]['title']
        except (IndexError, KeyError):
            raise Exception("Could not find a title in given DR rule")
        if self.queryset.filter(title=title):
            obj = self.queryset.filter(title=title).first()
            self.kwargs['pk'] = obj.id
            return super(DetectionRuleViewSet, self).update(
                request, *self.args, **self.kwargs
            )
        return super(DetectionRuleViewSet, self).create(
            request, *args, **kwargs
        )
