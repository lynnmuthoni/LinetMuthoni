# Generated by Django 5.0.6 on 2024-05-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('timeline', models.CharField(max_length=200)),
                ('programming_languages', models.CharField(max_length=200)),
                ('images', models.ImageField(upload_to='project_images/')),
                ('furtherdescription', models.TextField()),
            ],
        ),
    ]
