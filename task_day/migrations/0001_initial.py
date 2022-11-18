# Generated by Django 4.1.2 on 2022-10-28 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.player')),
            ],
        ),
    ]
