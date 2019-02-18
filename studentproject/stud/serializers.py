from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    father_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    mather_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    address= serializers.CharField(required=False, allow_blank=True, max_length=100)
    dob= serializers.DateField(default=0)
    age= serializers.IntegerField(default=0)
    _class=serializers.IntegerField(default=0)
    Speaks_Kannada = serializers.BooleanField(required=True)

    def create(self,validated_data):
        student= Student.objects.create(**validated_data)
        return student


    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.mather_name = validated_data.get('mather_name', instance.mather_name)
        instance.address = validated_data.get('address', instance.address)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.age = validated_data.get('age', instance.age)
        instance._class = validated_data.get('_class', instance._class)
        instance.Speaks_Kannada = validated_data.get('Speaks_Kannada', instance.Speaks_Kannada)


        instance.save()
        return instance
