# Generated by Django 2.0 on 2020-05-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_POSTS', '0006_auto_20200510_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
