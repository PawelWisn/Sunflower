# Generated by Django 4.1 on 2022-10-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField(default='', max_length=4000)),
                ('reviewed', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
