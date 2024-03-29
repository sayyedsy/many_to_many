# Generated by Django 2.2.6 on 2019-11-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='author',
            fields=[
                ('authorid', models.IntegerField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=35)),
                ('books', models.ManyToManyField(to='app1.book')),
            ],
            options={
                'db_table': 'author',
            },
        ),
    ]
