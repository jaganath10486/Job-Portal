from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    def __create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extrafields)
        user.set_password(make_password(password))
        print("Password", password)
        print("Password 1 ", make_password(password))
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extrafields):
        extrafields.setdefault('is_staff', False)
        return self.__create_user(email, password, **extrafields)

    def create_superuser(self, email, password, **extrafileds):
        extrafileds.setdefault('is_superuser', True)
        if(extrafileds.get('is_superuser')) is False:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.__create_user(email, password, **extrafileds)
    
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()
    
