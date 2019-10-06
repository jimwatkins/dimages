from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    comment_nature = models.CharField(max_length=200)
    comment_id = models.IntegerField
    comment_text = models.CharField(max_length=500)
    comment_user = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    objects = models.Manager() 
    def __str__(self):
        return self.comment_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'