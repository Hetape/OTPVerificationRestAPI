from django.db import models
from accounts.models import User
# Create your models here.
class Track(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    imgname = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self,*args,**kwargs):
    
        super(Track,self).save(*args,**kwargs)

    def __str__(self):
        return '%s--->%s(%s) : %s'%(self.user.get_full_name(),self.imgname,self.state,self.created_at)
    
    
    