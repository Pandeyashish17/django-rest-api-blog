# Generated by Django 4.1.2 on 2022-10-18 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_publisheddate_article_publishedat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='authorimage',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='imagetitle',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
    ]