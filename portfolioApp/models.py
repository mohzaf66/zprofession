from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Contact(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Service=models.CharField(max_length=50)
    Email=models.CharField(max_length=200)
    Phone=models.CharField(max_length=20)
    Company=models.CharField(max_length=100,null=True)
    Message=models.TextField()
    Date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.First_Name + " Contacted for " + self.Service + " at " + str(self.Date) 
    
class Post(models.Model):
    Title=models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=True,blank=True)
    Meta_Tags = models.CharField(max_length=200,null=True)
    Description=models.TextField()
    Category=models.CharField(max_length=50)
    Body=RichTextUploadingField()
    Date=models.DateField(auto_now_add=True)   
    Views=models.IntegerField(default=0,null=True)
    Likes=models.IntegerField(default=0,null=True)
    Dis_Likes=models.IntegerField(default=0,null=True)
    CommentsCounts=models.IntegerField(default=0,null=True)
    def __str__(self):
        return self.Title + " | " + str(self.Date)

def createslug(instance,new_slug=None):
    slug=slugify(instance.Title)
    if new_slug is not None:
        slug=new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return createslug(instance,new_slug=new_slug)
    return slug
def pre_save_post_receiver(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=createslug(instance)
pre_save.connect(pre_save_post_receiver,Post)

class Comment(models.Model):
    Post=models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=50,null=True)
    Body=models.TextField(null=True)
    Time=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.Post) + " | "  + self.Body + " | " + self.Name + " | " + str(self.Time)
    
class Website(models.Model):
    Name=models.CharField(max_length=20)
    Link=models.CharField(max_length=200)
    Customer=models.CharField(max_length=30)
    def __str__(self):
        return self.Name + " | " + self.Customer
        