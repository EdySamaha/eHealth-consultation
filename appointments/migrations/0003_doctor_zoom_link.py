# Generated by Django 3.1.7 on 2021-04-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20210410_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='zoom_link',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
