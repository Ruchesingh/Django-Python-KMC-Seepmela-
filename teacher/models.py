from django.db import models

# Create your models here.
class Grade(models.Model):
    name=models.CharField(max_length=20,help_text="enter grade name",verbose_name="Grade name")
    section=models.CharField(max_length=5,default='A')
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}-{self.section}'
    
    class Meta:
        db_table="grade"
        unique_together=['name','section']
        
class Teacher(models.Model):
    grade = models.ForeignKey(Grade,on_delete=models.SET_NULL, related_name="grade_teacher",null=True)
    name = models.CharField(max_length=60, help_text="teacher name")
    phone = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "teacher"