# Generated by Django 5.0.4 on 2024-04-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temlate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=200)),
                ('template_description', models.CharField(max_length=200)),
                ('template_data', models.ImageField(upload_to=None)),
            ],
        ),
    ]
