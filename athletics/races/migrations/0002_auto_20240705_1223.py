# Generated by Django 4.2.13 on 2024-07-05 12:23
from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations


def create_resultsmanagers_group(apps, schema_migration):
    """The function who will create the resultsmanagers groups without assigns existing users to the appropriate
    groups during migration"""

    # ensure that permissions have been created
    emit_post_migrate_signal(verbosity=1, interactive=False, db='default')

    # Use the apps.get_model() function to retrieve them
    Group = apps.get_model('auth', 'Group')

    # Create the resultsmanagers group
    resultsmanagers = Group(name='resultsmanagers')
    resultsmanagers.save()


class Migration(migrations.Migration):
    dependencies = [
        ("races", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_resultsmanagers_group)
    ]
