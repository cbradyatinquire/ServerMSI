from django.db import models
from datetime import datetime

class Interaction(models.Model):
    interaction_contents = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now())
    def __unicode__(self):
        return str(self.interaction_contents)

