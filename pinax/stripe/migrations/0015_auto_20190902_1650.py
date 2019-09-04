# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0014_auto_20180413_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='closed',
            field=models.NullBooleanField(default=None),
        ),
    ]
