# Generated by Django 2.2.2 on 2019-09-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezekielpost', '0002_auto_20190929_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='stage',
            field=models.IntegerField(choices=[(0, 'Planning'), ('Testing', 'Execution'), (2, 'Optimization')], default=1),
        ),
    ]
