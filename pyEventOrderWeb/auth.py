from django.contrib.auth.models import User

class OAuthBackend(object):

    def authenticate(self, code):
        user = User.objects.get(username='user')
        return user

    def get_user(self, user_id):
        return User.objects.get(pk=user_id)