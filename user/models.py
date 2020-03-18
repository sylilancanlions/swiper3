from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    """
    user data model
    """
    SEX = (
        ('M','male'),
        ('F','female'),
    )
    nickname = models.CharField(max_length=32,unique=True)
    phonenum = models.CharField(max_length=16,unique=True)
    sex = models.CharField(default='M',max_length=8,choices=SEX)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    # storage url address
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)


    @property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        times = today-birth_date
        return times.days // 365
    @property
    def profile(self):
        if'_profile' not in self.__dict__:
            self._profile,_ = Profile.objects.get_or_create(id=self.id)
        return self._profile

class Profile(models.Model):
    """
    user setting
    """
    SEX = (
        ('M', 'male'),
        ('F', 'female'),
    )

    min_distance = models.IntegerField(default=1,verbose_name='minimum search distance')
    max_distance = models.IntegerField(default=10,verbose_name='maximum search distance')
    min_dating_age = models.IntegerField(default=18,verbose_name='minimum dating age')
    max_dating_age = models.IntegerField(default=45,verbose_name='maximum dating age')
    dating_sex = models.CharField(default='F',max_length=8,choices=SEX,verbose_name='dating sex')
    vibration = models.BooleanField(default=True,verbose_name='whether vibrate')
    only_matche = models.BooleanField(default = True,verbose_name='only the matched can watch the album')
    auto_play = models.BooleanField(default = True,verbose_name='auto play video')
    location = models.CharField(max_length=32,verbose_name='target city')

