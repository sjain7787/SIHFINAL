# Generated by Django 4.0.2 on 2022-08-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_import1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import1',
            name='arrival',
            field=models.CharField(max_length=122),
        ),
    ]
