from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey('auth.User')
    STP_NAME= models.CharField(max_length=50,
    	choices = [ ('SNOWDON', 'Snowdon'),
        ('NORTH_DISPOSAL', 'North Disposal'),
        ('SUMMER_HILL', 'Summer Hill'),
        ('DHALLI', 'Dhalli'),
        ('SANJAULI_MALYANA', 'Sanjauli Malyana'),
        ('LALPANI', 'Lalpani') ],default = 'SNOWDON')
    #title = models.CharField(max_length=200)
    FLOW_RECEIVED = models.FloatField()
    IN_BOD = models.FloatField()
    IN_COD = models.FloatField()
    IN_pH = models.FloatField()
    IN_TSS = models.FloatField()
    IN_DO = models.FloatField()
    EF_BOD = models.FloatField()
    EF_COD = models.FloatField()
    EF_pH = models.FloatField()
    EF_TSS = models.FloatField()
    EF_DO = models.FloatField()

    COMMENTS = models.TextField(null=True, blank=True)
    
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.STP_NAME
