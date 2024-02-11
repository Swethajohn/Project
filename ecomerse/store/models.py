from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Category(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100)
	catogory = models.ForeignKey(Category, on_delete=models.CASCADE)
	description = models.TextField(null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='products/')

	def __str__(self):
		return self.name

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.quantity} x {self.product.name}'


# class CustomUser(AbstractUser):
#     pass


class CustomUser(AbstractUser):
    # ... other fields ...

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
    )
