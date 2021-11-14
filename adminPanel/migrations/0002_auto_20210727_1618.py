# Generated by Django 3.2.5 on 2021-07-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageURL',
            field=models.ImageField(default='img/icon.png', upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='productName',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='productLocation',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='productSpecification',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]