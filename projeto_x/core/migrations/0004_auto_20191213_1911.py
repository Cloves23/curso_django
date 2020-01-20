# Generated by Django 3.0 on 2019-12-13 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_naturalperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='addresses', related_query_name='address', to='core.Person', verbose_name='person')),
                ('street', models.CharField(max_length=100, verbose_name='street')),
                ('neighbourhood', models.CharField(max_length=100, verbose_name='neighbourhood')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('number', models.CharField(max_length=50, verbose_name='number')),
                ('complement', models.CharField(max_length=100, verbose_name='complement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='legalperson',
            name='municipal_registration',
            field=models.CharField(max_length=18, verbose_name='municipal registration'),
        ),
        migrations.AlterField(
            model_name='legalperson',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Person', verbose_name='person'),
        ),
        migrations.AlterField(
            model_name='legalperson',
            name='state_registration',
            field=models.CharField(max_length=18, verbose_name='state registration'),
        ),
        migrations.AlterField(
            model_name='naturalperson',
            name='birthday',
            field=models.DateField(verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='naturalperson',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='naturalperson',
            name='nationality',
            field=models.CharField(max_length=40, verbose_name='nationality'),
        ),
        migrations.AlterField(
            model_name='naturalperson',
            name='naturalness',
            field=models.CharField(max_length=30, verbose_name='naturalness'),
        ),
        migrations.AlterField(
            model_name='naturalperson',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Person', verbose_name='person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.CharField(max_length=16, verbose_name='document'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(max_length=30, verbose_name='nickname'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=16, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
    ]