# Generated by Django 4.0.2 on 2022-02-12 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_patient_password1_alter_patient_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='password2',
        ),
    ]