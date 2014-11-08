# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('venue_id', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
