from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class problems(models.Model):
    problem_title=models.CharField(max_length=100, default="--problemTitle--")
    problem_statement= models.TextField()
    test_cases = models.FileField(null='True')
    expected_output = models.FileField(null='True')

class submission(models.Model):
    problem=models.ForeignKey(problems,on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp= models.DateTimeField(auto_now_add=True)
    submitted_code=models.FileField()
    verdict=models.CharField(max_length=10, default='Running...')

