from rest_framework.serializers import ModelSerializer
from base.models import Exchange_Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Exchange_Room
        fields='__all__'