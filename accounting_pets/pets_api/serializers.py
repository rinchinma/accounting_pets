from rest_framework import serializers

from pets_api.models import Pet, PetPhoto


class PetPhotoSerializer(serializers.ModelSerializer):

    url = serializers.ImageField(source="photo")

    class Meta:
        model = PetPhoto
        fields = ("id", "url")

    def to_internal_value(self, data):
        resource_data = data["file"]

        return super().to_internal_value(resource_data)


class PetSerializer(serializers.ModelSerializer):

    photos = PetPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Pet
        fields = ("id", "name", "age", "type", "photos", "created_at")


class PhotoLoadSerializer(serializers.Serializer):

    file = serializers.ImageField()


class IdsSerializer(serializers.Serializer):

    ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1), allow_empty=False
    )
