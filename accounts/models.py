from django.db import models
# AbstractUserモデルをインポート
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    '''Userモデルを継承したカスタムユーザーモデル'''
    pass
# Create your models here.
