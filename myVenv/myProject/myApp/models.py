from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class UserProgress(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        progress_percentage = models.IntegerField(default=0)
        completed = models.BooleanField(default=False)  
        last_access = models.DateTimeField(auto_now=True)    

        def __str__(self):
            return f"{self.user.username} {self.course.title}: {self.progress_percentage}%"
        