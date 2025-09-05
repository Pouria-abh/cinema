from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from jalali_date import datetime2jalali, date2jalali
from account_module.models import User
from django.core.validators import MinValueValidator


# Create your models here.



class Gener(models.Model):
    
    title=models.CharField(max_length=100,verbose_name='ژانر')
    url_title=models.CharField(max_length=100,verbose_name='عنوان در url',null=True,blank=True)
    class Meta:
        verbose_name='ژانر'
        verbose_name_plural='ژانر ها'
     
    def __str__(self):
        return self.title
    
          

class Movie(models.Model):

    title=models.CharField(max_length=200,verbose_name='نام فیلم')
    image=models.ImageField(upload_to='images/',verbose_name='پوستر', null=True,blank=True)
    is_active=models.BooleanField(verbose_name='فعال / غیر فعال',default=False)
    short_description =models.TextField(verbose_name='توضیحات کوتاه', null=True)
    gener=models.ManyToManyField(Gener,verbose_name='ژانر')
    slug=models.SlugField(null=True,blank=True,verbose_name='عنوان در url',allow_unicode=True)
    expire_at=models.DateTimeField(null=True,blank=True,verbose_name='زمان انقضا')
    class Meta:
        verbose_name='فیلم'
        verbose_name_plural='فیلم ها'
     
    def __str__(self):
        return self.title
    
    
    
    @property
    def is_expired(self):
        return self.expire_at and self.expire_at < timezone.now()
    
        
        

class CinemaHall(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام سالن')
    capacity=models.PositiveIntegerField(verbose_name='ظرفیت سالن')    
    
    class Meta:
        verbose_name='سالن'
        verbose_name_plural='سالن ها'
    
    def __str__(self):
        return self.name
    
    
        

class ShowTimes(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,verbose_name='فیلم')
    hall=models.ForeignKey(CinemaHall,on_delete=models.CASCADE,verbose_name='سالن')
    time=models.DateTimeField(verbose_name='زمان نمایش')
    parice=models.DecimalField(max_digits=8,decimal_places=2,default=0,verbose_name='قیمت',validators=[MinValueValidator(0)])
    
    class Meta:
        verbose_name='سانس'
        verbose_name_plural='سانس ها'
    
    def __str__(self):
        return f"{self.movie.title} - {self.hall.name} - {self.time.strftime('%H:%M')}"
    
    def get_jalali_create_date(self):
        return date2jalali(self.time)

    def get_jalali_time(self):
        hour = self.time.hour
        time_str = self.time.strftime('%H:%M')

        if 6 <= hour < 12:
            period = "صبح"
        elif 12 <= hour < 18:
            period = "بعدازظهر"
        elif 18 <= hour < 22:
            period = "عصر"
        else:
            period = "شب"

        return f"({period}) {time_str} "
    
    
class Seats(models.Model):
    seat_number=models.CharField(max_length=20,verbose_name='شماره صندلی')
    hall=models.ForeignKey(CinemaHall,on_delete=models.CASCADE,verbose_name='سالن')
    time=models.ForeignKey(ShowTimes,on_delete=models.CASCADE,verbose_name='زمان نمایش')
    extra_charge=models.IntegerField(default=0,verbose_name='هزینه اضافی صندلی')
    def __str__(self):
        return self.seat_number
    
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['seat_number','hall','time'],name='unique_seat')
        ]
        verbose_name='صندلی'
        verbose_name_plural='صندلی ها'
    
        

class Ticket(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,verbose_name='فیلم')
    hall=models.ForeignKey(CinemaHall,on_delete=models.CASCADE,verbose_name='سالن')
    time=models.ForeignKey(ShowTimes,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='زمان نمایش')
    seat=models.OneToOneField(Seats,on_delete=models.CASCADE,verbose_name='صندلی')
    final_price=models.DecimalField(max_digits=8,decimal_places=2,default=0,verbose_name='قیمت ثبت شده')
    def __str__(self):
        return f"{str(self.user.username)} / {self.movie.title} / {self.time.strftime('%H:%M')}"
    
    class Meta:
        verbose_name='بلیط'
        verbose_name_plural='بلیط ها'        