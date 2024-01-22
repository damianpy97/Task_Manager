from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class Task(models.Model):

    STATUS = [
        ('new', 'new'),
        ('in_progress', 'in progress'),
        ('finished', 'finished')]

    name = models.CharField(max_length=80, blank=False)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=11, choices=STATUS, default='new')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'task'

    def __str__(self):
        return self.name


class History(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=80, blank=False)
    status = models.CharField(max_length=11)
    description = models.TextField(blank=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_type = models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    class Meta:
        managed = False
        db_table = 'task_manager_historicaltask'
