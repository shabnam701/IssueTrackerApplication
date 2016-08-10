from django.db import models
from django.utils import timezone
from datetime import date


class Post(models.Model):
    COMPLEXITY=(('1','one'),('2','two'),('3','three'),('4','four'),('5','five'),('6','six'),('7','seven'),('8','eight'),('9','nine'),('10','ten'))
    STATUS=(('NEW','new'),('INPROGRESS','inprogress'),('RESOLVED','resolved'),('FEEDBACK','feedback'),('CLOSED','closed'))
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    dueDate = models.DateField(
            blank=True, null=True)
    createdOn = models.DateField(
            default=date.today())
    complexity=models.CharField(max_length=1,choices=COMPLEXITY)
    status=models.CharField(max_length=20,choices=STATUS)

    def addissue(self):
        self.createdOn = timezone.now()
        self.save()

    def __str__(self):
        return self.title
