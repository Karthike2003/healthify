# Generated by Django 4.0.2 on 2022-02-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_special_remove_doctor_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_image',
            field=models.ImageField(blank=True, default='doctors/user-default.png', max_length=200, null=True, upload_to='doctors/'),
        ),
    ]