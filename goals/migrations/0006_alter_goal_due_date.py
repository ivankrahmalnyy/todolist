# Generated by Django 4.0.1 on 2022-12-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_alter_goalcategory_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
