# Generated by Django 4.2.14 on 2024-07-24 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.artist'),
        ),
    ]