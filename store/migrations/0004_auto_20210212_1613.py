# Generated by Django 3.1.6 on 2021-02-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210212_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='texte',
            old_name='msg',
            new_name='para',
        ),
        migrations.AddField(
            model_name='texte',
            name='titre',
            field=models.CharField(max_length=500, null=True),
        ),
    ]