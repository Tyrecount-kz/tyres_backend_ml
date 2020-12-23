from rest_framework import serializers
from users.models import ShopUser
from shop.models import Car

class ShopUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopUser
        exclude = ['password']
        read_only_field = ['id','first_name','last_name']
    
class ShopUserPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    titleId = serializers.SerializerMethodField(read_only=True)
    
    def get_titleId(self,obj):
        return obj.car_model + " " + str(obj.id)

    class Meta:
        model = Car
        fields = ['id','car_model','titleId','price','mileage','engine_volume']
        read_only_field = ['titleId']