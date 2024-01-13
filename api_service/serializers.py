from rest_framework.serializers import Serializer,ModelSerializer

from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        