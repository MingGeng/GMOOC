# Generated by Django 2.0.2 on 2018-03-06 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_auto_20180305_1857'),
        ('courses', '0010_auto_20180306_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='课程讲师'),
        ),
    ]
