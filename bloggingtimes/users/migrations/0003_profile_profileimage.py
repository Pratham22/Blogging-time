# Generated by Django 3.0.2 on 2020-09-16 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200914_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]