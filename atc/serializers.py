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


    globals()[f'{name}Serializer'] = Serializer

