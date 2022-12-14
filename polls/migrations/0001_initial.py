# Generated by Django 4.1 on 2022-08-11 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=12)),
                ('phone_code', models.IntegerField(max_length=4)),
                ('tag', models.TextField(max_length=10)),
                ('timezone', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_start', models.DateTimeField()),
                ('msg_text', models.TextField(max_length=500)),
                ('property_filter', models.TextField(max_length=14)),
                ('mailing_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_start', models.DateTimeField()),
                ('msg_status', models.IntegerField(choices=[(0, 'Отправляется'), (1, 'Сообщение доставлено'), (2, 'Error')], default=0)),
                ('id_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.client')),
                ('id_mailing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.mailing')),
            ],
        ),
    ]
