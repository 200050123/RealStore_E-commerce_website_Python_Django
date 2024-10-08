# Generated by Django 3.1.4 on 2022-07-18 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear')], max_length=10)),
                ('product_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
