# Generated by Django 4.1.5 on 2023-01-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='author_picture',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='article',
            name='coverImage',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='image_article',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
