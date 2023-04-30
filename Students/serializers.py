from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, StudentInformation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name'
        )


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'department', 'rollNo', 'batch')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        student = Student.objects.create(user=user, **validated_data)
        return student


class StudentInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInformation
        fields = '__all__'

    def create(self, validated_data):
        student = self.context['request'].user.student
        student_information = StudentInformation.objects.create(
            student=student, **validated_data)
        return student_information
