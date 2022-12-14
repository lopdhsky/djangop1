from django.db import models
from django.contrib.auth.models import AbstractUser # 회원관리 모듈

# Create your models here. 
# 여기는 데이터베이스라고 생각하면 됨


class 아이디(AbstractUser):
    pass

class Sale(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE) # 데이터 테이블 사이의 관계를 정리함

class Person(models.Model):
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)

    def __str__(self):
        return self.회원.username
        