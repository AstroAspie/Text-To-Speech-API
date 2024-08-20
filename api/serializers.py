from rest_framework import serializers
from .models import TextToSpeech


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextToSpeech
        fields = ['length_minutes']
        extra_kwargs = {"length_minutes": {"read_only": True}}
