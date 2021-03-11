# Generated by Django 3.0.6 on 2021-03-11 03:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webtestapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchModelForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('mail', models.EmailField(max_length=255, verbose_name='メール')),
                ('gender', models.CharField(max_length=16, verbose_name='性別')),
                ('department', models.CharField(max_length=255, verbose_name='部署')),
                ('year', models.CharField(default=0, max_length=16, verbose_name='社歴')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
    ]
