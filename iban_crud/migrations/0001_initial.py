# Generated by Django 4.0 on 2021-12-28 22:49

from django.db import migrations, models
import django.db.models.deletion
import localflavor.generic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='IBANUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('iban', localflavor.generic.models.IBANField(include_countries=None, max_length=34, use_nordea_extensions=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
