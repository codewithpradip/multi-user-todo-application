from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES = [
    ('C', 'Completed'),
    ('P', 'Pending'),
    ]

    PRIORITY_CHOICES = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ]
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    date = models.DateField(auto_now_add=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    priority =  models.CharField(max_length=5, choices=PRIORITY_CHOICES)