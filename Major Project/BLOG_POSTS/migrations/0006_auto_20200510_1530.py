# Generated by Django 2.0 on 2020-05-10 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_POSTS', '0005_post_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='username',
        ),
    ]
