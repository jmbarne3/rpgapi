# Generated by Django 4.2.3 on 2023-08-01 13:27

from django.db import migrations, models
import django.db.models.deletion

def create_default_job(apps, schema_editor):
    Job = apps.get_model('characters', 'Job')
    Job(
        id=1,
        name='Freelancer',
        description='Default job for all new characters',
        strength_mod=1.0,
        dexterity_mod=1.0,
        vitality_mod=1.0,
        agility_mod=1.0,
        intelligence_mod=1.0,
        mind_mod=1.0
    ).save()

def remove_default_job(apps, schema_editor):
    Job = apps.get_model('characters', 'Job')
    try:
        Job.objects.get(pk=1).delete()
    except Job.DoesNotExist:
        print("Default job did not exist so was not deleted.")


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_character_experience_points_character_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('strength_mod', models.FloatField()),
                ('dexterity_mod', models.FloatField()),
                ('vitality_mod', models.FloatField()),
                ('agility_mod', models.FloatField()),
                ('intelligence_mod', models.FloatField()),
                ('mind_mod', models.FloatField()),
            ],
        ),
        migrations.RunPython(
            create_default_job,
            remove_default_job
        ),
        migrations.AddField(
            model_name='character',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='characters.job'),
            preserve_default=False,
        ),
    ]
