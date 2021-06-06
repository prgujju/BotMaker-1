# Generated by Django 3.1.4 on 2021-03-17 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0014_datasource_datasourcetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bots.datasource'),
        ),
        migrations.AddField(
            model_name='datasource',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='bots.datasourcetype'),
            preserve_default=False,
        ),
    ]
