# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import storages.backends.s3boto


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.FileField(storage=storages.backends.s3boto.S3BotoStorage(location=b'media'), null=True, upload_to=b'uploads/categories/thumbnails', blank=True),
        ),
    ]
