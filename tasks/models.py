from django.db import models
from django.contrib.auth.models import User

#includes fields for the task's title, description, due date, priority, assignment, and status, along with a string representation method that returns the task's title

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    STATUS_CHOICES = [
        ('TO_DO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='TO_DO')

    def __str__(self):
        return self.title

#Define the Comment Model which links to the Task model

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.created_date}'

