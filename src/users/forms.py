from django_registration.forms import RegistrationForm
from users.models import ShopUser

class ShopUserForm(RegistrationForm):

    class Meta(RegistrationForm):
        model = ShopUser
        exclude = ['password','is_admin','is_staff','is_superuser',]