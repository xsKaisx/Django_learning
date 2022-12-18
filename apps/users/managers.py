from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, username: str, password: str, **options):
        normalized_username = self.normalize_email(username)
        res = {
            **{'username': normalized_username},
            **options
        }
        user = self.model(**res)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, username:str, password:str, **options):
        options.setdefault('is_active', True)
        options.setdefault('is_staff', True)
        return self._create_user(username, password, **options)

    def create_superuser(self, username:str, password:str, **options):
        options.setdefault('is_active', True)
        options.setdefault('is_staff', True)
        options.setdefault('is_admin', True)
        options.setdefault('is_superuser', True)

        return self._create_user(username, password, **options)