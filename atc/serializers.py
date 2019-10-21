from rest_framework import serializers
import atc.models as models


class CategorySerializer(serializers.ModelSerializer):

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
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


class PlatformSerializer(serializers.ModelSerializer):

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
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


class LogTypeSerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    class Meta:
        model = models.LogType
        fields = '__all__'

    def create(self, validated_data):
        log_type = models.LogType.objects.get_or_create(
            name=validated_data.get('name')
        )
        return log_type

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


class ChannelSerializer(serializers.ModelSerializer):

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
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


class ProviderSerializer(serializers.ModelSerializer):

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
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


class VolumeSerializer(serializers.ModelSerializer):

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
        log_field = models.LogField.objects.get_or_create(
            name=validated_data.get('name')
        )
        return log_field

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


class StageSerializer(serializers.ModelSerializer):

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
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


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


class TagSerializer(serializers.ModelSerializer):

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
        return value.name

    def to_internal_value(self, data):
        return {"name": data}


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
            logging_policy = models.LoggingPolicy.objects.get_or_create(
                title=validated_data['title']
            )
            logging_policy.description = validated_data.get('description')
            logging_policy.default = validated_data.get('default')
            logging_policy.configuration = validated_data.get('configuration')
        else:
            logging_policy = instance

        if logging_policy.eventID:
            logging_policy.eventID.set([])
        if logging_policy.references:
            logging_policy.references.set([])

        vol = models.Volume.objects.get_or_create(name=volume['name'])
        logging_policy.volume_id = vol[0].id

        for item in eventID:
            eid = models.EventID.objects.get_or_create(id=item['id'])
            logging_policy.eventID.add(eid[0])
        for item in references:
            ref = models.References.objects.get_or_create(url=item['url'])
            logging_policy.references.add(ref[0])

        logging_policy.save()
        return logging_policy

    def update(self, instance, validated_data):
        return self.create(validated_data, instance=instance)

# class DataNeededSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.DataNeeded
#         fields = '__all__'


class EnrichmentSerializer(serializers.ModelSerializer):

    # Translate IDs to corresponding field values
    data_needed = serializers.CharField(
        source='data_needed.title',
        allow_null=True, allow_blank=True
    )
    data_to_enrich = serializers.CharField(
        source='data_to_enrich.title',
        allow_null=True, allow_blank=True
    )
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


class DataNeededSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    references = ReferencesSerializer(many=True)
    logging_policy = serializers.ListField(write_only=True)
    platform = PlatformSerializer()
    log_type = LogTypeSerializer()
    channel = ChannelSerializer()
    provider = ProviderSerializer()
    log_field = LogFieldSerializer(many=True)

    class Meta:
        model = models.DataNeeded
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        category_name = validated_data['category']['name']
        category = models.Category.objects.get_or_create(name=category_name)[0]

        platform_name = validated_data['platform']['name']
        platform = models.Platform.objects.get_or_create(name=platform_name)[0]

        log_type_name = validated_data['log_type']['name']
        log_type = models.LogType.objects.get_or_create(name=log_type_name)[0]

        channel_name = validated_data['channel']['name']
        channel = models.Channel.objects.get_or_create(name=channel_name)[0]

        provider_name = validated_data['provider']['name']
        provider = models.Provider.objects.get_or_create(name=provider_name)[0]

        obj_dict = {
            "category": category,
            "platform": platform,
            "log_type": log_type,
            "channel": channel,
            "provider": provider,
            "title": validated_data['title'],
            "description": validated_data['description'],
            "sample": validated_data['sample']

        }

        data_needed = models.DataNeeded.objects.get_or_create(**obj_dict)[0]
        fields = validated_data['log_field']
        for field_o in fields:
            field = models.LogField.objects.get_or_create(
                name=field_o['name']
            )[0]
            data_needed.log_field.add(field)

        refs = validated_data['references']
        for ref in refs:
            references = models.References.objects.get_or_create(url=ref)[0]
            data_needed.references.add(references)

        for lp_name in validated_data['logging_policy']:
            lp = models.LoggingPolicy.objects.get_or_create(title=lp_name)[0]
            data_needed.logging_policy.add(lp)
        data_needed.save()
        return data_needed


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
