# Generated by Django 3.2.6 on 2022-02-16 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0003_userimportfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]