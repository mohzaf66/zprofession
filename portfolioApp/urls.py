from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Admin Panel Title
admin.site.site_header="Zprofession Admin"
admin.site.site_title="Zprofession Admin "

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('blog/',views.blog, name='blog'),
    path('blogdetail/<str:slug>/', views.blogdetail, name="blogdetail"),
    #cdeditor
    path('ckeditor',include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
