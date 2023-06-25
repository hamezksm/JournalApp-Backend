from rest_framework import serializers
from models import *

#serialize you models here

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'username', 'date_of_birth', 'gender', 'email', 'password']
        
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'