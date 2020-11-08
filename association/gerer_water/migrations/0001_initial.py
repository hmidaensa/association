# Generated by Django 3.1.2 on 2020-10-31 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sasion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annne', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Periode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.IntegerField()),
                ('saison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerer_water.sasion')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('nom_arabic', models.CharField(max_length=50)),
                ('num_counteur', models.CharField(max_length=50)),
                ('num_maison', models.IntegerField()),
                ('date_adhesion', models.DateField()),
                ('date_resiliation', models.DateField()),
                ('cin', models.CharField(max_length=12)),
                ('status', models.CharField(max_length=20)),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerer_water.lieu')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mountant_default', models.IntegerField()),
                ('mountant_consomme', models.IntegerField()),
                ('total', models.IntegerField()),
                ('old_counteur', models.IntegerField()),
                ('new_counteur', models.IntegerField()),
                ('factute_paye', models.IntegerField()),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerer_water.member')),
                ('periode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerer_water.periode')),
            ],
        ),
    ]
