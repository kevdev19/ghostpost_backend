from django.db import models
from django.utils.timezone import now

class RoastBoast(models.Model):
    POST_TYPE_CHOICES = [('B', 'Boast'), ('R', 'Roast'),]
    post_type = models.CharField(max_length=1, choices=POST_TYPE_CHOICES)
    content = models.CharField(max_length=280)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    create_time = models.DateTimeField(default=now, editable=False)
    update_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.content
    


