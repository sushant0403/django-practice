# Generated by Django 4.1.4 on 2023-01-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_comment_review_comment_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avg_rating',
            field=models.FloatField(blank=True, default=0),
        ),
    ]