from django.db import models

class SentItem(models.Model):
    moment = models.DateTimeField(auto_now = True)
    data = models.TextField()
    
    
    