# Generated by Django 3.1.5 on 2021-06-27 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0012_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.post'),
        ),
    ]
