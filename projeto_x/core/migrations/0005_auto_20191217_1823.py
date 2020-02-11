# Generated by Django 3.0 on 2019-12-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191217_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='addresses', related_query_name='address', to='core.Tag', verbose_name='tags'),
        ),
    ]