# Generated by Django 3.1.6 on 2021-02-08 00:37

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20210208_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=files.models.userimage_profile_file_path),
        ),
    ]
