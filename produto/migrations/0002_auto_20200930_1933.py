# Generated by Django 3.1 on 2020-09-30 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='tipo_link',
            field=models.CharField(choices=[('P', 'Por produto'), ('M', 'Por marca'), ('C', 'Por categoria'), ('H', 'Por campanha')], default='', max_length=1),
        ),
    ]
