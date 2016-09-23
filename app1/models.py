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
    FLOW_RECEIVED = models.CharField(max_length=200)
    IN_BOD = models.CharField(max_length=200)
    IN_COD = models.CharField(max_length=200)
    IN_pH = models.CharField(max_length=200)
    IN_TSS = models.CharField(max_length=200)
    IN_DO = models.CharField(max_length=200)
    EF_BOD = models.CharField(max_length=200)
    EF_COD = models.CharField(max_length=200)
    EF_pH = models.CharField(max_length=200)
    EF_TSS = models.CharField(max_length=200)
    EF_DO = models.CharField(max_length=200)

    COMMENTS = models.TextField(null=True, blank=True)
    
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.STP_NAME
