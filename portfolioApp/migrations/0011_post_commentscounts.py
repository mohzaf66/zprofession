# Generated by Django 3.1.5 on 2021-06-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0010_post_dis_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='CommentsCounts',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
