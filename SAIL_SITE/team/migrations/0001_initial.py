# Generated by Django 3.2.4 on 2021-12-25 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('linkeden', models.URLField(blank=True, null=True)),
                ('pic', models.URLField(max_length=1000)),
                ('is_alumnus', models.BooleanField(default=True)),
                ('year', models.PositiveSmallIntegerField(default=2021)),
                ('pic_id', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.position')),
            ],
        ),
    ]
