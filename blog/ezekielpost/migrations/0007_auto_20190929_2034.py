# Generated by Django 2.2.2 on 2019-09-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezekielpost', '0006_auto_20190929_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='img/post/personal.png', upload_to='post/'),
        ),
    ]
