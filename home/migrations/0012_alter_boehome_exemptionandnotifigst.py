# Generated by Django 4.0.2 on 2022-08-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_cetheadind_boehome_cetheading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boehome',
            name='exemptionandnotifigst',
            field=models.FileField(upload_to='Uploads/'),
        ),
    ]
