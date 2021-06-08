# Generated by Django 3.2.3 on 2021-06-04 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0009_auto_20210602_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='cookbook',
        ),
        migrations.RemoveField(
            model_name='tips',
            name='cookbook',
        ),
        migrations.AddField(
            model_name='instruction',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cookbook.recipe'),
        ),
        migrations.AddField(
            model_name='tips',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cookbook.recipe'),
        ),
    ]
