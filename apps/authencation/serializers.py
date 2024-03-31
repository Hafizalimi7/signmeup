from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
        style={'input_type': 'password'}
    )
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username','email', 'password','date_of_birth']
    extra_kwargs = {'password': {'write_only': True}}
    
  def create(self, validated_data):
    user = User.objects.create(
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      username = validated_data['username'],
      email = validated_data['email'],
      date_of_birth = validated_data['date_of_birth']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
