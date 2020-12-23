from rest_framework import generics, mixins
from shop.models import Car
from .serializers import CarSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated,IsAuthenticatedOrReadOnly, SAFE_METHODS
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q, F

class ShopCarRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        car_id = self.kwargs.get('pk')
        """
        if self.request.method == 'GET':
            car = Car.objects.all().update(views=F('views') + 1)
            print(car[0].views)
        """
        #Update car views
        car_detail = Car.objects.get(id=car_id)
        car_detail.views += 1
        car_detail.save(update_fields=['views'])

        return Car.objects.all()


class ShopCarListAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        qs = Car.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            """ for postgres
            qs = Car.objects.annotate(
                search=SearchVector('car_model') + SearchVector('user_id') 
                                                 + SearchVector('shell') 
                                                 + SearchVector('color')
                                                 + SearchVector('custom_clear')
                                                 + SearchVector('custom_clear')
                                                 + SearchVector('gear')
                                                 + SearchVector('city')
            ).filter(search=query"""
            qs = qs.filter(Q(car_model__icontains=query) | Q(shell_icontains=query) | Q(city_icontains=query)).distinct()
        return qs