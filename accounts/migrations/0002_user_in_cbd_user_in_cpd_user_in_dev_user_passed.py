# Generated by Django 4.2.7 on 2023-11-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='in_cbd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='in_cpd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='in_dev',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]