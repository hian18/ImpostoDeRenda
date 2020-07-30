# Generated by Django 3.0.8 on 2020-07-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpostoDeRenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rendimento_a', models.FloatField()),
                ('rendimento_b', models.FloatField()),
                ('isento', models.BooleanField()),
                ('aliquota', models.FloatField()),
                ('deducao', models.FloatField()),
                ('ano_referencia', models.IntegerField()),
            ],
        ),
    ]