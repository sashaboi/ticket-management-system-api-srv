from rest_framework import serializers
from .models import User, Site, Ticket


class TicketSerializer(serializers.ModelSerializer):
    creator_email = serializers.ReadOnlyField(source='creator.email')
    site_name = serializers.ReadOnlyField(source='site.name')

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'status', 'creator_email', 'site_name']
        read_only_fields = ['creator_email', 'site_name']


class SiteSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Site
        fields = ['id', 'name', 'owner_email']
        read_only_fields = ['owner_email']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        site = Site.objects.create(**validated_data)
        return site


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
