from csa.models.user import User
from csa.models.core import Cart


def get_company_user():
    return User.objects.get(pk=1)


def get_user_cart(user_id):
    return Cart.objects.get_or_create(user_id=user_id)[0]
