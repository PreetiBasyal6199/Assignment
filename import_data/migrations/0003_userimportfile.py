# Generated by Django 3.2.6 on 2022-02-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0002_auto_20220216_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImportFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_import', models.FileField(upload_to='temp')),
            ],
        ),
    ]
