# Generated by Django 2.2.24 on 2021-10-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0038_project_is_top'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='sort',
            field=models.IntegerField(default=9999, verbose_name='排序'),
        ),
    ]
