import inspect

from rest_framework import serializers
import atc.models as models


class CategorySerializer(serializers.ModelSerializer):
    pass

class PlatformSerializer(serializers.ModelSerializer):
    pass

class LogTypeSerializer(serializers.ModelSerializer):
    pass

class ChannelSerializer(serializers.ModelSerializer):
    pass

class ProviderSerializer(serializers.ModelSerializer):
    pass

class VolumeSerializer(serializers.ModelSerializer):
    pass

class LogFieldSerializer(serializers.ModelSerializer):
    pass

class StageSerializer(serializers.ModelSerializer):
    pass

class EventIDSerializer(serializers.ModelSerializer):
    pass

class TagSerializer(serializers.ModelSerializer):
    pass

class ReferenceSerializer(serializers.ModelSerializer):
    pass

class LoggingPolicySerializer(serializers.ModelSerializer):
    pass

class DataNeededSerializer(serializers.ModelSerializer):
    pass

class EnrichmentSerializer(serializers.ModelSerializer):
    pass

class ResponseActionSerializer(serializers.ModelSerializer):
    pass

class ResponsePlaybookSerializer(serializers.ModelSerializer):
    pass

class DetectionRuleSerializer(serializers.ModelSerializer):
    pass


for name, model_o in inspect.getmembers(models):
    # a very dumb decision
    class Serializer(serializers.ModelSerializer):
        class Meta:
            model = model_o
            fields = '__all__'
    if "dataneeded" not in name.lower():
        globals()[f'{name}Serializer'] = Serializer


class DataNeededSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reference = ReferenceSerializer(many=True)
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
            field = models.LogField.objects.get_or_create(name=field_o['name'])[0]
            data_needed.log_field.add(field)

        refs = validated_data['reference']
        for ref in refs:
            reference = models.Reference.objects.get_or_create(url=ref)[0]
            data_needed.reference.add(reference)

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

            dr = models.DetectionRule.objects.create(title=validated_data['title'],
                                                     description=validated_data['description'] )
            for dn in dn_list:
                dr.data_needed.add(dn)
            dr.save()
        return dr

