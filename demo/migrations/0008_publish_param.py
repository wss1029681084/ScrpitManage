# Generated by Django 2.1.4 on 2019-05-10 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='publish',
            name='param',
            field=models.CharField(default=1, max_length=500, verbose_name='参数'),
            preserve_default=False,
        ),
    ]
