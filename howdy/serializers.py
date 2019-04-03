from rest_framework import serializers
from .models import Experience
from .models import Picture

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'post', 'salary')

class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('pic_name', 'image')

    def get_image_url(self, obj):
        return obj.image.url