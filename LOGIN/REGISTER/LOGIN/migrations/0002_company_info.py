# Generated by Django 2.1.14 on 2019-11-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=100)),
                ('Company_Address', models.CharField(max_length=300)),
                ('Company_Email', models.EmailField(max_length=254)),
                ('Comapny_Country', models.CharField(max_length=60)),
                ('Comapny_State', models.CharField(max_length=50)),
                ('Company_City', models.CharField(max_length=50)),
                ('Company_Contact', models.CharField(max_length=10)),
                ('Company_Category', models.CharField(max_length=200)),
            ],
        ),
    ]