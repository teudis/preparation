# Generated by Django 4.1.3 on 2022-12-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0002_alter_medication_url_image'),
        ('drones', '0002_alter_drone_weigth_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='medications',
            field=models.ManyToManyField(to='medications.medication'),
        ),
    ]