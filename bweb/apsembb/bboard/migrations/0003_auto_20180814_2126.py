# Generated by Django 2.1 on 2018-08-15 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20180814_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_text',
            new_name='comment_text',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post_user',
            new_name='comment_user',
        ),
    ]
