# Generated by Django 4.0.5 on 2022-06-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_userresults_delete_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresults',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
