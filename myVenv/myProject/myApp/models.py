from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Course

class User(AbstractUser):
    pass

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class CourseProgress(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        progress_percentage = models.IntegerField(default=0)
        completed = models.BooleanField(default=False)  
        last_access = models.DateTimeField(auto_now=True)   

        class UserPrefences(models.Model):
            user = models.OneToOneField(User, on_delete=models.CASCADE)
            favorite_subjects = models.TextField (help_text="Comma-separated list of course IDs")

        class Meta:
            unique_together = ('user','course')    

        def get_subject_list(self):
            return [s.strip()for s in self.favourite_subjects.split(",")]   

        def __str__(self):
            return f"{self.user.username} {self.course.title}: {self.progress_percentage}%"
     
        
       