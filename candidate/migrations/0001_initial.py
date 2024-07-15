# Generated by Django 4.2 on 2024-07-13 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(db_index=True, max_length=15, unique=True)),
                ('email', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
