# Generated by Django 4.0.4 on 2022-08-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_codregistro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codregistro',
            field=models.CharField(default='000000', max_length=6),
        ),
    ]