from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime

def validate_file_extension (value):
    import os
    from django.core.exceptions import ValidationError
    ext=os.path.splitext(value.name)[1]
    valid_extensions=['.jpg','.png','.jpng']
    if not ext.lower() in valid_extensions:
        raise ValidationError('unsoppuetrd fileformat')

class UserProfile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.FileField(upload_to='files/user-avatar/',null=True , blank=True,validators=[validate_file_extension])
    description=models.CharField(max_length=512,null=False, blank=False)
    

class Article(models.Model):
    title=models.CharField(max_length=128,null=False,blank=False)
    cover=models.FileField(upload_to='files/article_cover/',null=False,blank=False,validators=[validate_file_extension])
    content=RichTextField()
    created_at=models.DateTimeField(default=datetime.now,blank=False)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    author=models.ForeignKey(UserProfile,on_delete=False)
    promote = models.BooleanField(default=False)
    

class category(models.Model):
    title=models.CharField(max_length=1128,null=False,blank=False)
    cover=models.FileField(upload_to='files/category-cover/',null=False,blank=False,validators=[validate_file_extension])
    
