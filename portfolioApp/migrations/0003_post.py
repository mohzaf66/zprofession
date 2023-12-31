# Generated by Django 3.1.5 on 2021-06-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0002_contact_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Category', models.CharField(max_length=50)),
                ('Body', models.TextField()),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
