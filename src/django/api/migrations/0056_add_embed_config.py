# Generated by Django 2.2.19 on 2021-04-05 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0055_add_report_switch'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbedConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(default='600', help_text='The width of the embedded map.', max_length=200)),
                ('height', models.CharField(default='400', help_text='The height of the embedded map.', max_length=200)),
                ('color', models.CharField(blank=True, help_text='The color of the embedded map.', max_length=200, null=True)),
                ('font', models.CharField(blank=True, help_text='The font of the embedded map.', max_length=200, null=True)),
                ('show_other_contributor_information', models.BooleanField(default=False, help_text='Whether or not to show other contributor information.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='embed_config',
            field=models.OneToOneField(help_text='The embedded map configuration for the contributor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.EmbedConfig'),
        ),
        migrations.AddField(
            model_name='historicalcontributor',
            name='embed_config',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The embedded map configuration for the contributor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api.EmbedConfig'),
        ),
        migrations.CreateModel(
            name='EmbedField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(help_text='The column name of the field.', max_length=200)),
                ('display_name', models.CharField(help_text='The name to display for the field.', max_length=200)),
                ('visible', models.BooleanField(default=False, help_text='Whether or not to display this field.')),
                ('order', models.IntegerField(help_text='The sort order of the field.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('embed_config', models.ForeignKey(help_text='The embedded map configuration which uses this field', on_delete=django.db.models.deletion.CASCADE, to='api.EmbedConfig')),
            ],
            options={
                'unique_together': {('embed_config', 'order')},
            },
        ),
    ]
