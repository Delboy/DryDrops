# Generated by Django 3.2 on 2022-05-27 14:31

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(max_length=1024, validators=[profanity.validators.validate_is_profane]),
        ),
    ]