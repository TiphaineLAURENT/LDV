# Generated by Django 3.0.6 on 2020-05-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20200525_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='vetement',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]