# Generated by Django 4.0.6 on 2023-08-23 04:45

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_ordering_category_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('ordering', models.IntegerField(default=0)),
                ('special', models.BooleanField(default=False)),
                ('publish_date', models.DateTimeField()),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
