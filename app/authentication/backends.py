from datetime import datetime, timezone, timedelta

from jose import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'bearer'

    def authenticate(self, request):
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None
        if len(auth_header) == 1:
            return None
        elif len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
        except Exception:
            msg = "Authentication error. Can't decode token"
            raise exceptions.AuthenticationFailed(msg)
        
        try:
            expire = payload['exp']
        except KeyError:
            msg = "Authentication error. Bad token."
            raise exceptions.AuthenticationFailed(msg)

        try:
            expire = int(expire)
        except ValueError:
            msg = "Authentication error. Bad Token"
            raise exceptions.AuthenticationFailed(msg)

        if expire - datetime.now(timezone.utc).timestamp() <= 0:
            msg = "Authentication error. Token is expired."
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(email=payload['sub'])
        except User.DoesNotExist:
            msg = 'A user with this email and password was not found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)
        
        return user, token
    