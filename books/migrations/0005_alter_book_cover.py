# Generated by Django 4.0 on 2022-01-14 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(null=True, upload_to='media/covers/'),
        ),
    ]
