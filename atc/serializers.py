from rest_framework import serializers
import atc.models as models
# from pprint import pprint
from atc.atc_dr_utils import fill_DN
from json import dumps as json_dumps
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Platform
        fields = '__all__'


class LogTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LogType
        fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Channel
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Provider
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Volume
        fields = '__all__'


class LogFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LogField
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Stage
        fields = '__all__'


class EventIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EventID
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = '__all__'


class ReferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.References
        fields = '__all__'

# ################################################################ #
# ################### Nested ATC Serializers ##################### #
# ################################################################ #


class CategorySerializerNested(serializers.CharField):

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


class PlatformSerializerNested(serializers.CharField):

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


class LogTypeSerializerNested(serializers.CharField):

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


class ChannelSerializerNested(serializers.CharField):

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


class ProviderSerializerNested(serializers.CharField):

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


class VolumeSerializerNested(serializers.CharField):

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


class LogFieldSerializerNested(serializers.ModelSerializer):

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


class StageSerializerNested(serializers.CharField):

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


class EventIDSerializerNested(serializers.ModelSerializer):

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


class TagSerializerNested(serializers.ModelSerializer):

    name = serializers.CharField()

    class Meta:
        model = models.Tag
        fields = '__all__'

    def create(self, validated_data):
        tag = models.Tag.objects.get_or_create(
            name=validated_data.get('name')
        )
        return tag

    def update(self, instance, validated_data):
        return self.create(validated_data)

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return data


class ReferencesSerializerNested(serializers.ModelSerializer):

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
    volume = VolumeSerializerNested(
        source='volume.name', allow_null=True, required=False
    )
    eventID = EventIDSerializerNested(
        many=True, allow_null=True, required=False
    )
    references = ReferencesSerializerNested(
        many=True, allow_null=True, required=False
    )

    class Meta:
        model = models.LoggingPolicy
        fields = '__all__'

    def create(self, validated_data, instance=None):
        if 'eventID' in validated_data:
            eventID = validated_data.pop('eventID')
        else:
            eventID = []
        if 'volume' in validated_data:
            volume = validated_data.pop('volume')
        else:
            volume = []
        if 'references' in validated_data:
            references = validated_data.pop('references')
        else:
            references = []
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
    category = CategorySerializerNested(source='category.name')
    platform = PlatformSerializerNested(source='platform.name')
    type = LogTypeSerializerNested(source='type.name')
    channel = ChannelSerializerNested(source='channel.name')
    provider = ProviderSerializerNested(source='provider.name')
    loggingpolicy = LoggingPolicyViewSerializer(
        many=True, allow_null=True, required=False
    )
    references = ReferencesSerializerNested(
        many=True, allow_null=True, required=False)
    fields = LogFieldSerializerNested(
        many=True, allow_null=True, required=False)
    eventID = EventIDSerializerNested(
        many=True, allow_null=True, required=False
    )

    class Meta:
        model = models.DataNeeded
        fields = '__all__'

    def create(self, validated_data, instance=None):
        category = validated_data.pop('category')
        platform = validated_data.pop('platform')
        type = validated_data.pop('type')
        channel = validated_data.pop('channel')
        provider = validated_data.pop('provider')
        if 'references' in validated_data:
            references = validated_data.pop('references')
        else:
            references = []
        if 'loggingpolicy' in validated_data:
            loggingpolicy = validated_data.pop('loggingpolicy')
        else:
            loggingpolicy = []
        if 'fields' in validated_data:
            fields = validated_data.pop('fields')
        else:
            fields = []
        if not instance:
            dataneeded = models.DataNeeded.objects.get_or_create(
                title=validated_data['title']
            )[0]
        else:
            dataneeded = instance

        dataneeded.description = validated_data.get('description')
        dataneeded.sample = validated_data.get('sample')

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

        if dataneeded.references:
            dataneeded.references.set([])
        if dataneeded.fields:
            dataneeded.fields.set([])
        if dataneeded.loggingpolicy:
            dataneeded.loggingpolicy.set([])
        if dataneeded.eventID:
            dataneeded.eventID.set([])

        # special case (EventID from a title)
        try:
            eid = int(validated_data['title'].split("_")[2])
            obj = models.EventID.objects.get_or_create(id=eid)[0]
            dataneeded.eventID.add(obj.id)
        except ValueError:
            # No EventID in the title
            pass

        for item in references:
            obj = models.References.objects.get_or_create(url=item['url'])[0]
            dataneeded.references.add(obj)

        for item in fields:
            obj = models.LogField.objects.get_or_create(name=item['name'])[0]
            dataneeded.fields.add(obj)

        omit_lps = ["none", "todo", "to-do"]

        for item in loggingpolicy:
            try:
                obj = models.LoggingPolicy.objects.get(title=item['title'])
            except:
                if item['title'].lower() in omit_lps:
                    continue
                dataneeded.delete()
                raise serializers.ValidationError(
                    f"Logging Policy {item['title']} not found. "
                    "Push it first before referencing it."
                )
            dataneeded.loggingpolicy.add(obj)

        dataneeded.save()
        return dataneeded

    def update(self, instance, validated_data):
        return self.create(validated_data, instance=instance)


class DataNeededViewSerializer(serializers.ModelSerializer):
    """
    This serializer is to be used when nested
    """

    class Meta:
        model = models.DataNeeded
        fields = ["title", ]

    def to_representation(self, value):
        return value.title

    def to_internal_value(self, data):
        return {"title": data}


class EnrichmentListSerializer(serializers.ModelSerializer):
    """
    Dirty solution as I don't know how to point to "self" in serializer
    """

    title = serializers.CharField()

    class Meta:
        model = models.Enrichment
        fields = ["title", ]

    def to_representation(self, value):
        return value.title

    def to_internal_value(self, data):
        return {"title": data}


class EnrichmentSerializer(serializers.ModelSerializer):

    data_needed = DataNeededViewSerializer(many=True)
    data_to_enrich = DataNeededViewSerializer(
        many=True, allow_null=True, required=False)
    requirements = EnrichmentListSerializer(
        many=True, allow_null=True, required=False)
    references = ReferencesSerializerNested(
        many=True, allow_null=True, required=False)
    new_fields = LogFieldSerializerNested(
        many=True, allow_null=True, required=False)

    class Meta:
        model = models.Enrichment
        fields = '__all__'

    def create(self, validated_data, instance=None):
        data_needed = validated_data.pop('data_needed')
        if 'data_to_enrich' in validated_data:
            data_to_enrich = validated_data.pop('data_to_enrich')
        else:
            data_to_enrich = []
        if 'requirements' in validated_data:
            requirements = validated_data.pop('requirements')
        else:
            requirements = []
        if 'references' in validated_data:
            references = validated_data.pop('references')
        else:
            references = []
        if 'new_fields' in validated_data:
            new_fields = validated_data.pop('new_fields')
        else:
            new_fields = []

        if not instance:
            enrichment = models.Enrichment.objects.get_or_create(
                title=validated_data['title']
            )[0]
        else:
            enrichment = instance

        enrichment.description = validated_data.get('description')
        enrichment.author = validated_data.get('author')
        enrichment.config = validated_data.get('config')
        if enrichment.data_needed:
            enrichment.data_needed.set([])
        if enrichment.data_to_enrich:
            enrichment.data_to_enrich.set([])
        if enrichment.requirements:
            enrichment.requirements.set([])
        if enrichment.references:
            enrichment.references.set([])
        if enrichment.new_fields:
            enrichment.new_fields.set([])

        for item in data_needed:
            try:
                obj = models.DataNeeded.objects.get(title=item['title'])
            except:
                raise serializers.ValidationError(
                    f"Data Needed {item['title']} not found. "
                    "Push it first before referencing it."
                )
            enrichment.data_needed.add(obj)

        for item in data_to_enrich:
            try:
                obj = models.DataNeeded.objects.get(title=item['title'])
            except:
                raise serializers.ValidationError(
                    f"Data Needed {item['title']} not found. "
                    "Push it first before referencing it."
                )
            enrichment.data_to_enrich.add(obj)

        for item in requirements:
            try:
                obj = models.Enrichment.objects.get(title=item['title'])
            except:
                raise serializers.ValidationError(
                    f"Enrichment {item['title']} not found. "
                    "Push it first before referencing it."
                )
            enrichment.requirements.add(obj)

        for item in references:
            obj = models.References.objects.get_or_create(url=item['url'])
            enrichment.references.add(obj[0])

        for item in new_fields:
            obj = models.LogField.objects.get_or_create(name=item['name'])
            enrichment.new_fields.add(obj[0])

        enrichment.save()
        return enrichment

    def update(self, instance, validated_data):
        return self.create(validated_data, instance=instance)


class ResponseActionListSerializer(serializers.ModelSerializer):
    """
    Dirty solution as I don't know how to point to "self" in serializer
    """

    title = serializers.CharField()

    class Meta:
        model = models.ResponseAction
        fields = ["title", ]

    def to_representation(self, value):
        return value.title

    def to_internal_value(self, data):
        return {"title": data}


class ResponseActionSerializer(serializers.ModelSerializer):

    # Translate IDs to corresponding field values
    references = ReferencesSerializerNested(
        allow_null=True, required=False, many=True
    )
    stage = serializers.CharField(
        source='stage.name',
        allow_null=True, allow_blank=True
    )
    linked_ra = ResponseActionListSerializer(
        allow_null=True, required=False, many=True
    )
    creation_date = serializers.CharField(
        allow_null=True, allow_blank=True
    )

    class Meta:
        model = models.ResponseAction
        fields = '__all__'

    def create(self, validated_data, instance=None):

        if 'references' in validated_data:
            references = validated_data.pop('references')
        else:
            references = []

        if 'stage' in validated_data:
            stage = validated_data.pop('stage')
        else:
            stage = 'unknown'

        if 'linked_ra' in validated_data:
            linked_ra = validated_data.pop('linked_ra')
        else:
            linked_ra = []

        if not instance:
            raction = models.ResponseAction.objects.get_or_create(
                title=validated_data['title']
            )[0]
        else:
            raction = instance

        if raction.references:
            raction.references.set([])

        if raction.linked_ra:
            raction.linked_ra.set([])

        obj = models.Stage.objects.get_or_create(name=stage)[0]
        raction.stage = obj

        raction.title = validated_data.get("title")
        raction.description = validated_data.get("description")
        raction.author = validated_data.get("author")
        raction.workflow = validated_data.get("workflow")

        if validated_data.get("creation_date"):
            str_time = validated_data.get("creation_date")
            try:
                raction.creation_date = datetime.strptime(str_time, "%d.%m.%Y")
            except ValueError:
                # Could not parse, place default value
                pass

        for item in references:
            obj = models.References.objects.get_or_create(url=item['url'])
            raction.references.add(obj[0])

        for item in linked_ra:
            try:
                obj = models.ResponseAction.objects.get(title=item['title'])
            except:
                raise serializers.ValidationError(
                    f"Response Action {item['title']} not found. "
                    "Push it first before referencing it."
                )
            raction.linked_ra.add(obj)
        raction.save()
        return raction

    def update(self, instance, validated_data):
        return self.create(validated_data, instance=instance)


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


class DetectionRuleSerializer(serializers.ModelSerializer):

    raw_rule = serializers.JSONField()
    tag = TagSerializerNested(
        allow_null=True, required=False, many=True
    )
    references = ReferencesSerializerNested(
        allow_null=True, required=False, many=True
    )
    data_needed = DataNeededViewSerializer(
        allow_null=True, required=False, many=True
    )
    description = serializers.CharField(
        allow_null=True, required=False
    )
    severity = serializers.CharField(
        allow_null=True, required=False
    )
    status = serializers.CharField(
        allow_null=True, required=False
    )
    title = serializers.CharField(
        allow_null=True, required=False
    )

    class Meta:
        model = models.DetectionRule
        fields = '__all__'

    def create(self, validated_data, instance=None):
        raw_rule = validated_data.pop('raw_rule')

        try:
            title = raw_rule[0]['title']
        except:
            raise serializers.ValidationError("Title is missing")

        try:
            description = raw_rule[0]['description']
        except:
            raise serializers.ValidationError("Description is missing")

        severity = raw_rule[0].get('severity', 'unknown')
        if severity == 'unknown':
            severity = raw_rule[0].get('level', 'unknown')
        dev_status = raw_rule[0].get('status', 'unknown')

        if not instance:
            detection_rule = models.DetectionRule.objects.get_or_create(
                title=title
            )[0]
        else:
            detection_rule = instance

        detection_rule.description = description

        tags = raw_rule[0].get('tags', [])
        references = raw_rule[0].get('references', [])

        detection_rule.severity = severity
        detection_rule.status = dev_status
        detection_rule.author = raw_rule[0].get('author', "unknown")
        detection_rule.raw_rule = json_dumps(raw_rule)

        if detection_rule.tag:
            detection_rule.tag.set([])
        if detection_rule.references:
            detection_rule.references.set([])

        for url in references:
            obj = models.References.objects.get_or_create(url=url)
            detection_rule.references.add(obj[0])

        for name in tags:
            obj = models.Tag.objects.get_or_create(name=name)
            detection_rule.tag.add(obj[0])

        detection_rule.save()

        fill_DN(detection_rule)

        return detection_rule

    def update(self, instance, validated_data):
        return self.create(validated_data, instance=instance)
