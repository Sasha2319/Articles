# Generated by Django 3.1.7 on 2021-06-20 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='cDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата публикации'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, default='', upload_to='img'),
        ),
    ]
