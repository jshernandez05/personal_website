# Generated by Django 4.1.3 on 2022-11-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FilePathField(),
        ),
    ]
