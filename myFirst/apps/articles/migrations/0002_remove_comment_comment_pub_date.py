# Generated by Django 3.1.7 on 2021-03-16 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_pub_date',
        ),
    ]
