# Generated by Django 3.2.19 on 2023-05-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trained', '0007_admin_panel_welcome_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_panel',
            name='color_theme',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
