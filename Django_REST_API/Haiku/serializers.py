from rest_framework import serializers

from .models import HaikuModel

class HaikuSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = HaikuModel
        fields = '__all__'

    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)