# Generated by Django 2.0.2 on 2018-03-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseresource',
            options={'verbose_name': '课程资源', 'verbose_name_plural': '课程资源'},
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='name',
            field=models.CharField(max_length=100, verbose_name='课程资源名'),
        ),
    ]
