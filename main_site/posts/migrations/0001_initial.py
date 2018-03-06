# Generated by Django 2.0.2 on 2018-03-05 12:53

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.upload_location, width_field='width_field')),
                ('second_image', models.FileField(blank=True, null=True, upload_to=posts.models.upload_location)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('taged', models.CharField(blank=True, default=None, max_length=24, null=True)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]