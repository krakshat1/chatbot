# Generated by Django 4.0.4 on 2023-05-24 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trained', '0004_mymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin_panel',
        ),
        migrations.RemoveField(
            model_name='menuss',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='node',
            name='parent',
        ),
        migrations.DeleteModel(
            name='user_panel',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.DeleteModel(
            name='Menuss',
        ),
        migrations.DeleteModel(
            name='Node',
        ),
    ]