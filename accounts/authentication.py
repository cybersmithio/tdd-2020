from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):

    def authenticate(self, uid):
        print("PasswordlessAuthenticationBackend trying to authenticate UID:", uid)
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        print("PasswordlessAuthenticationBackend.get_user looking for email:", email)
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None