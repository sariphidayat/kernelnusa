# Generated by Django 3.2.3 on 2022-08-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0002_auto_20220827_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalentImportData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('domicilie', models.CharField(blank=True, max_length=200, null=True)),
                ('zone', models.CharField(blank=True, max_length=150, null=True)),
                ('education', models.CharField(blank=True, max_length=200, null=True)),
                ('majoring', models.CharField(blank=True, max_length=150, null=True)),
                ('applied_position', models.CharField(blank=True, max_length=150, null=True)),
                ('experience1', models.CharField(blank=True, max_length=255, null=True)),
                ('experience2', models.CharField(blank=True, max_length=255, null=True)),
                ('experience3', models.CharField(blank=True, max_length=255, null=True)),
                ('software_skill', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('expected_salary', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'talent_import_data',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='majoring',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='workposition',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]