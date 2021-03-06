# Generated by Django 2.0.1 on 2018-03-06 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corputils', '0005_cleanup_permissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corpstats',
            options={'permissions': (('view_corp_corpstats', 'Can view corp stats of their corporation.'), ('view_alliance_corpstats', 'Can view corp stats of members of their alliance.'), ('view_state_corpstats', 'Can view corp stats of members of their auth state.'), ('view_all_corpstats', 'Can view all corp stats, regardless of alliance.')), 'verbose_name': 'corp stats', 'verbose_name_plural': 'corp stats'},
        ),
    ]
