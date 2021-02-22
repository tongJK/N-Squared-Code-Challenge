from django.db import models


class Schools(models.Model):
    sc_name = models.CharField(max_length=20, unique=True)
    sc_max_st = models.IntegerField()
    sc_address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.sc_name

    def __unicode__(self):
        return self.sc_name


class Students(models.Model):
    st_first_name = models.CharField(max_length=20)
    st_last_name = models.CharField(max_length=20)
    st_ident = models.CharField(max_length=20, unique=True)
    st_school = models.ForeignKey(Schools, related_name='school', on_delete=models.CASCADE,
                                  null=False, blank=False)

    st_age = models.IntegerField(blank=True, null=True)
    st_class = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.st_ident} | {self.st_first_name} | {self.st_last_name}"

    def __unicode__(self):
        return f"{self.st_ident} | {self.st_first_name} | {self.st_last_name}"
