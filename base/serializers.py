from rest_framework import serializers
from .models import author,article,categories



class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = '__all__'


class categorySerializer(serializers.ModelSerializer):

    class Meta:
        model = categories
        fields = '__all__'



class articleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = article
        fields = '__all__'