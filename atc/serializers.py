from rest_framework import serializers
import atc.models as models
# from pprint import pprint


class CategorySerializer(serializers.CharField):

    name = serializers.CharField()

    class Meta:
        model = models.Category
        fields = '__all__'

    def create(self, validated_data):
        category = models.Category.objects.get_or_create(
            name=validated_data.get('name')
        )
        return category

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class PlatformSerializer(serializers.CharField):

    name = serializers.CharField()

    class Meta:
        model = models.Platform
        fields = '__all__'

    def create(self, validated_data):
        platform = models.Platform.objects.get_or_create(
            name=validated_data.get('name')
        )
        return platform

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class LogTypeSerializer(serializers.CharField):

    name = serializers.CharField()

    class Meta:
        model = models.LogType
        fields = '__all__'

    def create(self, validated_data):
        type = models.LogType.objects.get_or_create(
            name=validated_data.get('name')
        )
        return type

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class ChannelSerializer(serializers.CharField):

    name = serializers.CharField()

    class Meta:
        model = models.Channel
        fields = '__all__'

    def create(self, validated_data):
        channel = models.Channel.objects.get_or_create(
            name=validated_data.get('name')
        )
        return channel

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class ProviderSerializer(serializers.CharField):

    name = serializers.CharField()

    class Meta:
        model = models.Provider
        fields = '__all__'

    def create(self, validated_data):
        provider = models.Provider.objects.get_or_create(
            name=validated_data.get('name')
        )
        return provider

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class VolumeSerializer(serializers.CharField):

    name = serializers.CharField()

    class Meta:
        model = models.Volume
        fields = '__all__'

    def create(self, validated_data):
        volume = models.Volume.objects.get_or_create(
            name=validated_data
        )
        return volume

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class LogFieldSerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    class Meta:
        model = models.LogField
        fields = '__all__'

    def create(self, validated_data):
        field = models.LogField.objects.get_or_create(
            name=validated_data.get('name')
        )
        return field

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


class StageSerializer(serializers.CharField):

    name = serializers.CharField()

    class Meta:
        model = models.Stage
        fields = '__all__'

    def create(self, validated_data):
        stage = models.LogField.objects.get_or_create(
            name=validated_data.get('name')
        )
        return stage

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class EventIDSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = models.EventID
        fields = ['id', ]

    def create(self, validated_data):
        eid = models.EventID.objects.get_or_create(
            id=validated_data.get('id')
        )
        return eid

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value.id

    def to_internal_value(self, data):
        return {"id": data}


class TagSerializer(serializers.CharField):

    name = serializers.CharField()

    class Meta:
        model = models.Tag
        fields = '__all__'

    def create(self, validated_data):
        tag = models.LogField.objects.get_or_create(
            name=validated_data.get('name')
        )
        return tag

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class ReferencesSerializer(serializers.ModelSerializer):

    url = serializers.URLField()

    class Meta:
        model = models.References
        fields = '__all__'

    def create(self, validated_data):
        url = models.LogField.objects.get_or_create(
            url=validated_data.get('url')
        )
        return url

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value.url

    def to_internal_value(self, data):
        return {"url": data}

# ################################################################ #
# ################### Strict ATC Serializers ##################### #
# ################################################################ #


class LoggingPolicySerializer(serializers.ModelSerializer):

    # Translate IDs to corresponding field values
    volume = VolumeSerializer(source='volume.name', allow_null=True)
    eventID = EventIDSerializer(many=True, allow_null=True)
    references = ReferencesSerializer(many=True, allow_null=True)

    class Meta:
        model = models.LoggingPolicy
        fields = '__all__'

    def create(self, validated_data, instance=None):
        eventID = validated_data.pop('eventID')
        volume = validated_data.pop('volume')
        references = validated_data.pop('references')
        if not instance:
            loggingpolicy = models.LoggingPolicy.objects.get_or_create(
                title=validated_data['title']
            )[0]
        else:
            loggingpolicy = instance

        loggingpolicy.default = validated_data.get('default')
        loggingpolicy.description = validated_data.get('description')
        loggingpolicy.configuration = validated_data.get('configuration')

        if loggingpolicy.eventID:
            loggingpolicy.eventID.set([])
        if loggingpolicy.references:
            loggingpolicy.references.set([])

        vol = models.Volume.objects.get_or_create(name=volume['name'])
        loggingpolicy.volume_id = vol[0].id

        for item in eventID:
            eid = models.EventID.objects.get_or_create(id=item['id'])
            loggingpolicy.eventID.add(eid[0])
        for item in references:
            ref = models.References.objects.get_or_create(url=item['url'])
            loggingpolicy.references.add(ref[0])

        loggingpolicy.save()
        return loggingpolicy

    def update(self, instance, validated_data):
        return self.create(validated_data, instance=instance)


class LoggingPolicyViewSerializer(serializers.ModelSerializer):
    """
    This serializer is to be used when nested
    """

    class Meta:
        model = models.LoggingPolicy
        fields = ["title", ]

    def to_representation(self, value):
        return value.title

    def to_internal_value(self, data):
        return {"title": data}


class DataNeededSerializer(serializers.ModelSerializer):

    # Translate IDs to corresponding field values
    category = CategorySerializer(source='category.name')
    platform = PlatformSerializer(source='platform.name')
    type = LogTypeSerializer(source='type.name')
    channel = ChannelSerializer(source='channel.name')
    provider = ProviderSerializer(source='provider.name')
    loggingpolicy = LoggingPolicyViewSerializer(
        many=True, allow_null=True
    )
    references = ReferencesSerializer(many=True, allow_null=True)
    fields = LogFieldSerializer(many=True, allow_null=True)

    class Meta:
        model = models.DataNeeded
        fields = '__all__'

    def create(self, validated_data, instance=None):
        category = validated_data.pop('category')
        platform = validated_data.pop('platform')
        type = validated_data.pop('type')
        channel = validated_data.pop('channel')
        provider = validated_data.pop('provider')
        references = validated_data.pop('references')
        loggingpolicy = validated_data.pop('loggingpolicy')
        fields = validated_data.pop('fields')
        if not instance:
            dataneeded = models.DataNeeded.objects.get_or_create(
                title=validated_data['title']
            )[0]
        else:
            dataneeded = instance

        dataneeded.description = validated_data.get('description')
        dataneeded.sample = validated_data.get('sample')

        if dataneeded.loggingpolicy:
            dataneeded.loggingpolicy.set([])
        if dataneeded.references:
            dataneeded.references.set([])
        if dataneeded.fields:
            dataneeded.fields.set([])

        obj = models.Category.objects.get_or_create(name=category['name'])[0]
        dataneeded.category = obj
        obj = models.Platform.objects.get_or_create(name=platform['name'])[0]
        dataneeded.platform_id = obj.id
        obj = models.LogType.objects.get_or_create(name=type['name'])[0]
        dataneeded.type_id = obj.id
        obj = models.Channel.objects.get_or_create(name=channel['name'])[0]
        dataneeded.channel_id = obj.id
        obj = models.Provider.objects.get_or_create(name=provider['name'])[0]
        dataneeded.provider_id = obj.id

        for item in references:
            obj = models.References.objects.get_or_create(url=item['url'])
            dataneeded.references.add(obj[0])

        for item in fields:
            obj = models.LogField.objects.get_or_create(name=item['name'])
            dataneeded.fields.add(obj[0])

        for item in loggingpolicy:
            try:
                obj = models.LoggingPolicy.objects.get(title=item['title'])
            except:
                raise serializers.ValidationError("Logging Policy not found")
            dataneeded.loggingpolicy.add(obj)

        dataneeded.save()
        return dataneeded

    def update(self, instance, validated_data):
        return self.create(validated_data, instance=instance)


class EnrichmentSerializer(serializers.ModelSerializer):

    # Translate IDs to corresponding field values
    data_needed = DataNeededSerializer()
    data_to_enrich = DataNeededSerializer()
    requirement = serializers.CharField(
        source='requirement.name',
        allow_null=True, allow_blank=True
    )
    references = serializers.CharField(
        source='references.name',
        allow_null=True, allow_blank=True
    )
    new_field = serializers.CharField(
        source='new_field.name',
        allow_null=True, allow_blank=True
    )

    class Meta:
        model = models.Enrichment
        fields = '__all__'


class ResponseActionSerializer(serializers.ModelSerializer):

    # Translate IDs to corresponding field values
    references = serializers.CharField(
        source='references.name',
        allow_null=True, allow_blank=True
    )
    stage = serializers.CharField(
        source='stage.name',
        allow_null=True, allow_blank=True
    )
    linked_ra = serializers.CharField(
        source='linked_ra.title',
        allow_null=True, allow_blank=True
    )

    class Meta:
        model = models.ResponseAction
        fields = '__all__'


class ResponsePlaybookSerializer(serializers.ModelSerializer):

    # Translate IDs to corresponding field values
    tag = serializers.CharField(
        source='tag.name',
        allow_null=True, allow_blank=True
    )
    identification = serializers.CharField(
        source='identification.title',
        allow_null=True, allow_blank=True
    )
    containment = serializers.CharField(
        source='containment.title',
        allow_null=True, allow_blank=True
    )
    eradication = serializers.CharField(
        source='eradication.title',
        allow_null=True, allow_blank=True
    )
    recovery = serializers.CharField(
        source='recovery.title',
        allow_null=True, allow_blank=True
    )
    lessons_learned = serializers.CharField(
        source='lessons_learned.title',
        allow_null=True, allow_blank=True
    )

    class Meta:
        model = models.ResponsePlaybook
        fields = '__all__'


# class DetectionRuleSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.DetectionRule
#         fields = '__all__'


# ------------------------------------------------------------------
# --------- Don't know yet how to understand code below ------------
# ------------------------------------------------------------------

# for name, model_o in inspect.getmembers(models):
#     # a very dumb decision
#     class Serializer(serializers.ModelSerializer):
#         class Meta:
#             model = model_o
#             fields = '__all__'
#     if "dataneeded" not in name.lower():
#         globals()[f'{name}Serializer'] = Serializer


# class DataNeededSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     references = ReferencesSerializer(many=True)
#     loggingpolicy = serializers.ListField(write_only=True)
#     platform = PlatformSerializer()
#     type = LogTypeSerializer()
#     channel = ChannelSerializer()
#     provider = ProviderSerializer()
#     field = LogFieldSerializer(many=True)

#     class Meta:
#         model = models.DataNeeded
#         fields = '__all__'
#         depth = 2

#     def create(self, validated_data):
#         category_name = validated_data['category']['name']
#         category = models.Category.objects.get_or_create(name=category_name)[0]

#         platform_name = validated_data['platform']['name']
#         platform = models.Platform.objects.get_or_create(name=platform_name)[0]

#         type_name = validated_data['type']['name']
#         type = models.LogType.objects.get_or_create(name=type_name)[0]

#         channel_name = validated_data['channel']['name']
#         channel = models.Channel.objects.get_or_create(name=channel_name)[0]

#         provider_name = validated_data['provider']['name']
#         provider = models.Provider.objects.get_or_create(name=provider_name)[0]

#         obj_dict = {
#             "category": category,
#             "platform": platform,
#             "type": type,
#             "channel": channel,
#             "provider": provider,
#             "title": validated_data['title'],
#             "description": validated_data['description'],
#             "sample": validated_data['sample']

#         }

#         data_needed = models.DataNeeded.objects.get_or_create(**obj_dict)[0]
#         fields = validated_data['field']
#         for field_o in fields:
#             field = models.LogField.objects.get_or_create(
#                 name=field_o['name']
#             )[0]
#             data_needed.field.add(field)

#         refs = validated_data['references']
#         for ref in refs:
#             references = models.References.objects.get_or_create(url=ref)[0]
#             data_needed.references.add(references)

#         for lp_name in validated_data['loggingpolicy']:
#             lp = models.LoggingPolicy.objects.get_or_create(title=lp_name)[0]
#             data_needed.loggingpolicy.add(lp)
#         data_needed.save()
#         return data_needed


class DetectionRuleSerializer(serializers.ModelSerializer):
    data_needed_names = serializers.ListField(write_only=True)

    class Meta:
        model = models.DetectionRule
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        data_needed_names = validated_data['data_needed_names']
        dn_list = []
        for name in data_needed_names:
            queryset = models.DataNeeded.objects.filter(title=name)
            if len(queryset) > 0:
                dn_list.append(queryset.first())

            dr = models.DetectionRule.objects.create(
                title=validated_data['title'],
                description=validated_data['description']
            )
            for dn in dn_list:
                dr.data_needed.add(dn)
            dr.save()
        return dr
