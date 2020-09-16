from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64, verbose_name='部门名称')
    def __str__(self):
        return self.name

class Domain(models.Model):
    STASTUS = (
        ('checked','checked'),
        ('non-checked','non-checked')
    )
    domain_name = models.CharField(max_length=64, verbose_name='域名')
    person_in_charge = models.CharField(max_length=64, verbose_name='负责人')
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name = 'depart_web')
    status = models.CharField(max_length=64,choices=STASTUS,default='non-checked')
    def __str__(self):
        return self.domain_name

