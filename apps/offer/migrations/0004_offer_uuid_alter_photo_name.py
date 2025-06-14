# Generated by Django 5.2.3 on 2025-06-11 23:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_offer_rejected_reason_alter_offer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
