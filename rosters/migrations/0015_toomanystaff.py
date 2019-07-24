# Generated by Django 2.2.3 on 2019-07-24 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0014_nullable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daygroupday',
            options={'ordering': ('day',)},
        ),
        migrations.AlterModelOptions(
            name='staffruleshift',
            options={'ordering': ('position', 'shift__shift_type')},
        ),
        migrations.AddField(
            model_name='timeslot',
            name='max_staff',
            field=models.IntegerField(default=5),
        ),
    ]
