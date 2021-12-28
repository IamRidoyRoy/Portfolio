# Generated by Django 3.1 on 2021-12-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('body', models.CharField(max_length=5000)),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
