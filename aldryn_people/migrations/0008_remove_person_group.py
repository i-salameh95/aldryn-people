# -*- coding: utf-8 -*-


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_people', '0007_copy_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
    ]
