# Generated by Django 3.2.1 on 2021-05-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0014_auto_20210507_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Added_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]