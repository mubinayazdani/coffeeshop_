# Generated by Django 5.0.1 on 2024-05-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_contact_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]