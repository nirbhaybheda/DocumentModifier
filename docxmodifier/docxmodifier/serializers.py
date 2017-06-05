from rest_framework import serializers

class ModifySerializer(serializers.Serializer):
    replace = serializers.DictField()
