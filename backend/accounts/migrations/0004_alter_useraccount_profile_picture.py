# Generated by Django 4.2.2 on 2023-06-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_useraccount_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/profile_pictures/profile.png', null=True, upload_to='static/profile_pictures/'),
        ),
    ]