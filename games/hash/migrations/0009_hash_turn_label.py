# Generated by Django 3.0.3 on 2020-03-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hash', '0008_auto_20200220_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='hash',
            name='turn_label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
