# Generated by Django 3.1.6 on 2021-02-08 00:43

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20210208_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=files.models.userimage_profile_file_path),
        ),
    ]
