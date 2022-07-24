from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class problems(models.Model):
    problem_title=models.CharField(max_length=100, default="--problemTitle--")
    problem_statement= models.TextField()
    test_cases = models.FileField(upload_to='oj_test_cases/', null='True')
    expected_output = models.FileField(
    upload_to='oj_expected_outputs/', null='True')

class submissions(models.Model):
    problem=models.ForeignKey(problems,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, null='True')
    time_stamp= models.DateTimeField(auto_now_add=True)
    submitted_code=models.FileField(upload_to='oj_received/')
    verdict=models.CharField(max_length=10, default='Running...')

