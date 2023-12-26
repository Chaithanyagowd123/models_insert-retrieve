from django.db import models

# Create your models here.


class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    Location=models.CharField(max_length=100,null=False)
   
    def __str__(self):
        return str(self.deptno)


class Emp(models.Model):
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    Ename=models.CharField(max_length=100)
    Eid=models.IntegerField(unique=True,null=False)
    Sal=models.IntegerField(null=False)

    def __str__(self):
        return self.Ename
