# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'256')),
                ('xml', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_symbol', models.BooleanField(default=True, db_index=True)),
                ('stype', models.CharField(max_length=b'64')),
                ('created_by', models.ForeignKey(related_name='symbols', verbose_name=b'Created by', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
    ]
