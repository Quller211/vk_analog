# Generated by Django 4.2.3 on 2023-08-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='topic_images',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
