# Generated by Django 3.2.9 on 2021-12-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=18)),
                ('password', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=12)),
            ],
        ),
    ]
