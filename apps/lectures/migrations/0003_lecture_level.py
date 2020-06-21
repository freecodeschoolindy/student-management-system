# Generated by Django 3.0.7 on 2020-06-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_auto_20200614_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='level',
            field=models.IntegerField(choices=[(1, 'Level 1'), (2, 'Level 2')], default=1),
        ),
    ]