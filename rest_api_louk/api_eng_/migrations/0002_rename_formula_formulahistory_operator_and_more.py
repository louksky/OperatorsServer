# Generated by Django 4.0.3 on 2022-04-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_eng_', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulahistory',
            old_name='formula',
            new_name='operator',
        ),
        migrations.AddField(
            model_name='formulahistory',
            name='val1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='formulahistory',
            name='val2',
            field=models.TextField(blank=True, default=''),
        ),
    ]
