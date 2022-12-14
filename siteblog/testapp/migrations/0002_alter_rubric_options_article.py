# Generated by Django 4.1.1 on 2022-10-31 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rubric',
            options={'ordering': ['name'], 'verbose_name': 'рубрика(у)', 'verbose_name_plural': 'рубрики'},
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.rubric')),
            ],
            options={
                'verbose_name': 'статья(ю)',
                'verbose_name_plural': 'статьи',
                'ordering': ['name'],
            },
        ),
    ]
