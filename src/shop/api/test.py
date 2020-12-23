"""from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from shop.models import Car 

User = get_user_model()

class ShopCarAPITestCase(APITestCase):
    def setUp(self):
        user = User.object.create(username='testUser',email='testuser@kf.ru')
        user.set_password("TESTtest230")
        user.save()
        car = Car.objects.create(user=user,car_model='Toyota',release_year)
"""