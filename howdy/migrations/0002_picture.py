# Generated by Django 2.1.7 on 2019-04-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howdy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]