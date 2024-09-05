from django.db import models

class Report(models.Model):
    dept = models.CharField(max_length=50, verbose_name="Department")
    numStudents = models.IntegerField(verbose_name="Students")
    deptAvg= models.IntegerField(verbose_name="Average")
    publications = models.TextField(verbose_name="Publications")
    patents = models.TextField(verbose_name="Patents")
    achievements = models.TextField(verbose_name="Achievements")
    awards = models.TextField(verbose_name="Awards")
    alumniAchievements = models.TextField(verbose_name="Alumni Achievements")
    startups = models.TextField(verbose_name="Startups")