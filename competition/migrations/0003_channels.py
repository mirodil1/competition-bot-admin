# Generated by Django 4.1.2 on 2022-10-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_alter_telegramusers_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('invite_link', models.CharField(max_length=255, verbose_name='TASHRIF LINKI')),
                ('status', models.BooleanField(verbose_name='HOLATI')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="QO'SHILGAN VAQTI")),
            ],
            options={
                'verbose_name': 'Kanallar',
                'verbose_name_plural': 'Kanallar',
            },
        ),
    ]
