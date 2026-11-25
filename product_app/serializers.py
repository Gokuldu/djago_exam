from rest_framework import serializers
from product_app.models import productDb
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = productDb
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password"]
    def Create(self,validated_data):
        user = User.objects.Create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']

        )
        return user