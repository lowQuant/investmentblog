# Generated by Django 4.1.6 on 2023-02-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
