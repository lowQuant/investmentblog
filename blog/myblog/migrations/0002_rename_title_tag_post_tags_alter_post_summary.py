# Generated by Django 4.1.6 on 2023-02-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title_tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(),
        ),
    ]
