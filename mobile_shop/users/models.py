from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(default='default.png', upload_to='static/avatars')
    
    def history_default():
        return {'phones': []}
    
    shop_history = models.JSONField('Shopping history', default=history_default)
    
    def __str__(self):
        return self.user.username

