# Generated by Django 4.0.4 on 2022-05-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_user_phone_number_alter_listing_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Accessories', 'Аксесуари'), ('Antiques', 'Антикваріат'), ('Clothes', 'Речі'), ('Decoration', 'Декорації'), ('Electronics', 'Електроніка'), ('Valuables', 'Коштовності'), ('Other', 'Інше')], default='Other', max_length=11),
        ),
    ]
