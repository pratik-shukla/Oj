from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class problem(models.Model):
    problem_statement= models.TextField()
    # test_cases = models.FileField(default=)
    # expected_output= models.FileField()

class submission(models.Model):
    problem_id=models.ForeignKey(problem,on_delete=models.CASCADE)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp= models.DateTimeField(auto_now_add=True)
    submitted_code=models.FileField()
    verdict=models.CharField(max_length=10, default='Running...')

