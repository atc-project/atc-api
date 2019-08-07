from rest_framework import serializers
import atc.models as models


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
        model = models.Volume
        fields = '__all__'


class EventIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventID
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reference
        fields = '__all__'


class LoggingPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoggingPolicy
        fields = '__all__'


class DataNeededSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataNeeded
        fields = '__all__'


class EnrichmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrichment
        fields = '__all__'


class ResponseActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResponseAction
        fields = '__all__'


class ResponsePlaybookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResponsePlaybook
        fields = '__all__'


class DetectionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetectionRule
        fields = '__all__'



