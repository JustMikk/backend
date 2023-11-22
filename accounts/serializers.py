from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name',
                  'passed', 'in_cpd', 'in_dev', 'in_cbd']
        read_only_fields = ['id', 'email', 'first_name', 'last_name']
