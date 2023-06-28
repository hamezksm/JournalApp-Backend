from rest_framework import serializers
from .models import User, Journal

#serialize you models here

class UserSerializer(serializers.ModelSerializer):
    journals = serializers.PrimaryKeyRelatedField(many=True, queryset=Journal.objects.all()) 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email', 'password', 'journals']
        
class JournalSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Journal
        fields = ['user', 'title', 'content','timestamp']