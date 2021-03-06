# Generated by Django 2.2.2 on 2019-09-29 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ezekielpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('sales_point', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='stage',
            field=models.IntegerField(choices=[(0, 'Planning'), (1, 'Execution'), (2, 'Optimization')], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_post', to='ezekielpost.Department'),
        ),
    ]
