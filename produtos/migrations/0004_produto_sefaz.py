# Generated by Django 2.2.6 on 2019-10-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_categoria_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='sefaz',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
