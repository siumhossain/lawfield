import abc
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField

# Create your models here.
class User(AbstractUser):
    def save(self,*args,**kwargs):
        
        subject = 'welcome to LawField'
        message = f'Hi 🙋 {self.username}, Thank you for registering in LawField.Stay with us'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.email, ]
        send_mail( subject, message, email_from, recipient_list )
        super().save(*args,**kwargs) 
# class Law(MPTTModel):
#     act = models.CharField(max_length=50,default='',null=True,blank=True)
#     section_number = models.IntegerField(default=0)
#     title = models.CharField(max_length=250,null=True,blank=True)
#     description = models.TextField(null=True,blank=True)
#     omited = models.BooleanField(default=False)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    

#     def __str__(self):
#         return f'act no : {self.act} | section: {self.section_number} | title {self.title}'

#     class MPTTMeta:
#         order_insertion_by = ['act']


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Position(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class LawyerCategory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    position = models.ForeignKey(Position,on_delete=models.CASCADE,null=True,blank=True,default=1)
    area = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return f'{self.user.username} | {self.category.name}'

class About(models.Model):
    description = models.TextField()

class File(models.Model):
    text = models.CharField(max_length=300,null=True,blank=True)
    file = models.FileField(null=True,blank=True)



class Appointment(models.Model):
    fromUser = models.CharField(max_length=20)
    toUser = models.CharField(max_length=20)
    message = models.TextField()
    file = models.FileField(null=True,blank=True)


class Law(models.Model):
    act_no = models.CharField(max_length=100)
    title = models.CharField(max_length=400)
    date = models.DateField(null=True,blank=True)
    description = HTMLField(null=True,blank=True)

    def __str__(self):
        return f'{self.act_no} | {self.title}'

class LawDescription(models.Model):
    act_no = models.ForeignKey(Law,on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    
    description = HTMLField(null=True,blank=True)

    def __str__(self):
        return f'{self.title}'


class Quiz(models.Model):
    question = models.CharField(max_length=300)
    option_A = models.CharField(max_length=300)
    option_B = models.CharField(max_length=300)
    option_C = models.CharField(max_length=300)
    option_D = models.CharField(max_length=300)

    right_ans = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.id}| {self.question} | {self.right_ans}'

    
class AppointmentDetails(models.Model):
    lawyer = models.ForeignKey(User,on_delete=models.CASCADE)
    client = models.CharField(max_length=20)
    message = models.TextField()
    file = models.FileField(null=True,blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
         ordering = ['-created']
    
    
    

    

