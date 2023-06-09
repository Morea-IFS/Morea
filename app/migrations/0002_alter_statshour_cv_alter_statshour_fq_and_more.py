# Generated by Django 4.2.1 on 2023-05-19 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statshour',
            name='cv',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='statshour',
            name='fq',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='statshour',
            name='max',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='statshour',
            name='mean',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='statshour',
            name='median',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='statshour',
            name='min',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='statshour',
            name='mote',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.motes'),
        ),
        migrations.AlterField(
            model_name='statshour',
            name='std',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='statshour',
            name='tq',
            field=models.FloatField(blank=True),
        ),
    ]
