from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username','email', 'password','date_of_birth']
    
    def create(self, validated_data):
      user = User.objects.create(
        first_name = validated_data['first_name'],
        last_name = validated_data['last_name'],
        username = validated_data['username'],
      )
      user.save()
      return user