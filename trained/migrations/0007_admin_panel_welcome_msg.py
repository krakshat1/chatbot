# Generated by Django 3.2.19 on 2023-05-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trained', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_panel',
            name='welcome_msg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
