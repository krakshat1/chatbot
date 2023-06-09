# Generated by Django 4.0.4 on 2023-05-24 08:28

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trained', '0002_delete_admin_panel_remove_menuss_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='user_panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_label', models.CharField(blank=True, max_length=60, null=True)),
                ('input_type', models.CharField(blank=True, max_length=78, null=True)),
                ('parent_id', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('answer', models.CharField(blank=True, max_length=100, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trained.node')),
            ],
        ),
        migrations.CreateModel(
            name='Menuss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('answer', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='trained.menuss')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
