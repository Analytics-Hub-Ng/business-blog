# Generated by Django 2.2.2 on 2019-09-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezekielpost', '0003_auto_20190929_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='stage',
            field=models.IntegerField(choices=[(0, 'Planning'), ('Testing', 'Execution'), (2, 'Optimization')], default=0),
        ),
    ]
