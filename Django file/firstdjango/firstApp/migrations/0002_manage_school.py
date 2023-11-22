# Generated by Django 3.0.1 on 2020-03-25 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField()),
                ('school_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manage_id', models.IntegerField()),
                ('manage_name', models.CharField(max_length=20)),
                ('my_school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='firstApp.school')),
            ],
        ),
    ]