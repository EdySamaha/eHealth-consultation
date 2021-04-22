# Generated by Django 3.1.7 on 2021-04-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_remove_appointment_patientname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='doctorName',
            new_name='doctorname',
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientname',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
