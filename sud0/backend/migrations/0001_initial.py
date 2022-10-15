# Generated by Django 3.2.8 on 2022-06-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Working_Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='-', max_length=255, null=True)),
                ('url', models.URLField(default='https://sudrf.ru/index.php?id=300&act=go_ms_search&searchtype=ms&var=true&ms_type=ms&court_subj=0', max_length=255, null=True)),
                ('adress', models.CharField(default='-', max_length=255, null=True)),
                ('contact', models.CharField(default='-', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Working Site',
                'verbose_name_plural': 'Working Sites',
            },
        ),
    ]