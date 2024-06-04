from rest_framework import serializers
from .models import Users, Occupations


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'age', 'email', 'job_title']
        
class OccupationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupations
        fields = ['job_title', 'job_description']
        
        
