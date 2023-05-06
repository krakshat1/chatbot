# Generated by Django 4.0.4 on 2023-05-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trained', '0004_menu_answer1_submenu_answer1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='answer1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='answer1',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.RemoveField(
            model_name='submenu',
            name='menu',
        ),
        migrations.AddField(
            model_name='submenu',
            name='menu',
            field=models.ManyToManyField(null=True, related_name='submenues', to='trained.menu'),
        ),
    ]
