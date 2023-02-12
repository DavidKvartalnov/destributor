from .models import User
from rest_framework import serializers

from service.models import SectionKind, Section, SectionGroup, Service, Access


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('id', 'username', 'email', 'password')
        fields = '__all__'


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionKind
        fields = ('name',)


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name',)


class SectionSerializer(serializers.ModelSerializer):
    trainer = UserNameSerializer(read_only=True)

    class Meta:
        model = Section
        fields = ('name', 'trainer',)


class KindWithSectionSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=True)

    class Meta:
        model = SectionKind
        fields = ('name', 'section',)


class SectionGroupNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionGroup
        fields = ('id', 'name',)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'cost',)


class SingleSectionSerializer(serializers.ModelSerializer):
    trainer = UserNameSerializer(read_only=True)
    section_kind = KindSerializer(read_only=True)
    group = SectionGroupNameSerializer(many=True)
    service = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ('name', 'trainer', 'section_kind', 'group', 'service')


class SectionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name',)


class SectionGroupSerializer(serializers.ModelSerializer):
    section = SectionNameSerializer(read_only=True)
    customer = UserSerializer(many=True, read_only=True)

    class Meta:
        model = SectionGroup
        fields = (
            'id',
            'name',
            'section',
            'customer'
        )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class AccessSerializer(serializers.ModelSerializer):
    name = UserNameSerializer(many=True)
    service = ServiceSerializer(many=True)

    class Meta:
        model = Access
        fields = (
            'user',
            'service',
            'quantity',
            'is_subscribe',
            'is_active'
        )
