from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Faculty



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
                'username',
                'password',
                'first_name', 
                'last_name'
        )


class FacultySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Faculty
        fields = ('user','department','facultyId','batch')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        student = Faculty.objects.create(user=user, **validated_data)
        return student