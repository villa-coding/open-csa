from csa.models.user import User


def get_company_user():
    return User.objects.get(pk=1)
