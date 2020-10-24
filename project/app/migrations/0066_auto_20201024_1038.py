# Generated by Django 3.1.2 on 2020-10-24 03:38

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_auto_20201024_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuuho',
            name='huyen',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='tinh', chained_model_field='tinh', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuuho_reversed', to='app.huyen'),
        ),
        migrations.AlterField(
            model_name='cuuho',
            name='xa',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='huyen', chained_model_field='huyen', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuuho_reversed', to='app.xa'),
        ),
        migrations.AlterField(
            model_name='historicalhodan',
            name='huyen',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='tinh', chained_model_field='tinh', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app.huyen'),
        ),
        migrations.AlterField(
            model_name='historicalhodan',
            name='xa',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='huyen', chained_model_field='huyen', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app.xa'),
        ),
        migrations.AlterField(
            model_name='hodan',
            name='huyen',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='tinh', chained_model_field='tinh', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hodan_reversed', to='app.huyen'),
        ),
        migrations.AlterField(
            model_name='hodan',
            name='xa',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='huyen', chained_model_field='huyen', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hodan_reversed', to='app.xa'),
        ),
    ]
