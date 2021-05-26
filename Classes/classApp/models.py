from django.db import models

# Create your models here.

# sets up a database table through the creation of a class
class DjangoClasses(models.Model):
    title = models.CharField(max_length=50, default="", blank=True, null=False)
    course_number = models.IntegerField(default=0, null=False)
    instructor_name = models.CharField(max_length=50, default="", blank=True, null=False)
    duration = models.FloatField()

    # this allows us to access the database
    objects = models.Manager()

    # sets "title" as the display name for the current object instead of object
    def __str__(self):
        return self.title



