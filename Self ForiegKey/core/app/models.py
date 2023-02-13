from django.db import models

# Create your models here.
subjects=[
    ('English','English'),
    ('Math','Math'),
    ('Physics','Physics'),
    ('Zology','Zology'),
    ('Computer','Computer'),
]

class Teachers(models.Model):
    name=models.CharField(max_length=40)
    grade=models.IntegerField(default=14)
    subject=models.CharField(choices=subjects , max_length=50)
    headOfDepartment=models.ForeignKey('self', on_delete=models.CASCADE , blank=True , null=True)
    is_hod=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name