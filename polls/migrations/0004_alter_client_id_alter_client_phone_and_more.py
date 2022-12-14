# Generated by Django 4.1 on 2022-08-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_client_id_alter_mailing_id_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_code',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='tag',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='timezone',
            field=models.CharField(max_length=10),
        ),
    ]
