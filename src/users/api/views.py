from django.shortcuts import render
from .serializers import WishlistSerializer,ShopUserSerializer,ShopUserPostsSerializer
from rest_framework import generics,mixins,viewsets
from users.models import ShopUser
from shop.models import Car
from shop.api.serializers import CarSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly,IsAuthor
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

# Create your views here.
class ShopUserRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ShopUserSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly,IsAdminUser]
    
    def get_queryset(self):
        qs = ShopUser.objects.all()
        return qs

class ShopUserCreateAPIView(generics.CreateAPIView):
    serializer_class = ShopUserSerializer


class ShopUserListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ShopUserSerializer

    def get_queryset(self):
        qs = ShopUser.objects.all()
        return qs

class ShopUserPostsListView(generics.ListAPIView):  
    lookup_field = 'pk'
    serializer_class = ShopUserPostsSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        print(user_id)
        return Car.objects.all().filter(user_id=user_id)

class ShopUserPostCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthorOrReadOnly]

class ShopUserWishlistView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthorOrReadOnly]

    #def get_queryset(self):
        #user_id = self.kwargs.get('pk')
        #return Car.objects.all().filter(user_id=user_id, added_to_wishlist=1).order_by("price")
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        user_id = request.user.id
        queryset = self.get_queryset().filter(user_id=user_id,added_to_wishlist=1).order_by("price")
        serializer = WishlistSerializer(queryset, many=True)
        return Response(serializer.data)

class ShopUserWishlistAddView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = CarSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        car_id = self.kwargs.get('pk')
        """
        if self.request.method == 'GET':
            car = Car.objects.all().update(views=F('views') + 1)
            print(car[0].views)
        """
        #Update car views
        car_detail = Car.objects.get(id=car_id)
        car_detail.added_to_wishlist = 1
        car_detail.save(update_fields=['added_to_wishlist'])

        return Car.objects.all()

class ShopUserWishlistDeleteView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = CarSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        car_id = self.kwargs.get('pk')
        """
        if self.request.method == 'GET':
            car = Car.objects.all().update(views=F('views') + 1)
            print(car[0].views)
        """
        #Update car views
        car_detail = Car.objects.get(id=car_id)
        car_detail.added_to_wishlist = 0
        car_detail.save(update_fields=['added_to_wishlist'])

        return Car.objects.all()