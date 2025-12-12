from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Restaurant(models.Model):
  name=models.CharField(max_length=200)
  price=models.CharField(max_length=200)
  address=models.CharField(max_length=200)
  phone = models.CharField(max_length=20, blank=True)   # ← 追加
  description = models.TextField(blank=True) 
  img=CloudinaryField('image', blank=True, null=True)
  category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='restaurants')

  def __str__(self):
    return self.name

class Review(models.Model):
  restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='reviews')
  user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  rating=models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)]) #1～5の評価
  comment=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username} - {self.restaurant.name}"


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name} ({self.date} {self.time})"

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'restaurant')  # 重複登録を防止


class CustomUser(AbstractUser):
   is_premium = models.BooleanField(default=False)
   stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)