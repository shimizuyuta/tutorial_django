# Generated by Django 3.2.7 on 2021-09-01 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='tel_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='電話番号は半角英数のみで入力してください。例：09012345678', regex='^[0-9]+$')], verbose_name='電話番号'),
        ),
    ]