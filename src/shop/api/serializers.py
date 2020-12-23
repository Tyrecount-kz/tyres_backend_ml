from rest_framework import serializers

from shop.models import Car

class CarSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    def get_url(self, obj):
        return obj.get_api_detail_url()

    class Meta:
        model = Car
        fields = '__all__'
        read_only_field = ['id,user_id']


class WishlistSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    def get_url(self, obj):
        return obj.get_api_detail_url()

    class Meta:
        model = Car
        fields = '__all__'