from django.shortcuts import render
from .models import Contact,Post,Comment,Website

# Create your views here.

def index(request):
    websites=Website.objects.order_by('-id')[0:3]
    context={
        'websites':websites,
    }
    return render(request,'index.html',context)

def contact(request):
    if request.method=="POST":
        First_Name=request.POST.get('fname')
        Service=request.POST.get('service')
        Last_Name=request.POST.get('lname')
        Email=request.POST.get('email')
        Phone=request.POST.get('phone')
        Company=request.POST.get('company')
        Message=request.POST.get('message')
        contact=Contact(First_Name=First_Name,Service=Service,Last_Name=Last_Name,Email=Email,Phone=Phone,Company=Company,Message=Message)
        contact.save()
        return render(request, 'thankyou.html',{
            'First_Name':First_Name,
            'Service':Service
        })
    return render(request,'contact.html')

def thankyou(request):
    First_Name=request.POST.get('fname',default="Client")
    Service=request.POST.get('service',default="Service")
    context={
        'First_Name':First_Name,
        'Service':Service,
    }
    return render(request,'thankyou.html',context) 

def blog(request):
    posts=Post.objects.order_by('-id')
    context={
        'posts':posts,
    }
    return render(request,'blog.html',context)

def blogdetail(request,slug):
    post=Post.objects.get(slug=slug)
    comment=Comment.objects.filter(Post=post).order_by('-id')
    post.Views +=1
    if 'Like' in request.POST:
        post.Likes +=1
    if 'DisLike' in request.POST:
        post.Dis_Likes +=1   
    if 'Comment' in request.POST:
        post.CommentsCounts +=1
        Name=request.POST.get('name',default="Anonymous")
        Body=request.POST.get('comment')
        Comments=Comment(Name=Name,Body=Body,Post=post)
        Comments.save()      
    post.save()
    context={
        'post':post,
        'comment':comment,
    }
    return render(request,'blogdetail.html',context)