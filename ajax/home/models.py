from django.db import models
class citystate(models.Model):
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.state+" "+self.city
class Datas(models.Model):
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.state+" "+self.city