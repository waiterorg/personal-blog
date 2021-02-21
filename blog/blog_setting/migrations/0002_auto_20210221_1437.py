# Generated by Django 3.1.5 on 2021-02-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'تنظیم سایت', 'verbose_name_plural': 'تنظیمات سایت'},
        ),
        migrations.AddField(
            model_name='settings',
            name='active',
            field=models.BooleanField(default=False, verbose_name='فعال / غیر فعال'),
        ),
    ]
