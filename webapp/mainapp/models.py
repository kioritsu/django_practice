from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    name = models.CharField(max_length=16)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class BigCategory(models.Model):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SmallCategory(models.Model):
    name = models.CharField(max_length=32)
    big_category = models.ForeignKey(BigCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Method(models.Model):
    balance = models.BooleanField(help_text='収入ならTrue, 支出ならFalse')
    name = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Payment(models.Model):
    balance = models.BooleanField(help_text='収入ならTrue, 支出ならFalse')
    price = models.IntegerField() # 価格
    date = models.DateField() # 日付け
    method = models.ForeignKey(Method, on_delete=models.CASCADE) 
    small_category = models.ForeignKey(SmallCategory, on_delete=models.CASCADE) 
    member = models.ManyToManyField(Member)
    memo = models.TextField()

