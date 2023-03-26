from django.db import models
from .constants import TASK


class Task(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    status = models.IntegerField(choices=TASK.STATUS.CONSTANTS, default=TASK.STATUS.DEFAULT)
    priority = models.IntegerField(choices=TASK.PRIORITY.CONSTANTS, default=TASK.PRIORITY.DEFAULT)
    description = models.TextField(null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-priority', '-created_date')
        verbose_name = "MY TASK"
        verbose_name_plural = "MY TASKS"
