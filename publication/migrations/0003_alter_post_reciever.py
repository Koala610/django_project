# Generated by Django 4.0.3 on 2022-05-05 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_category', to='publication.category'),
        ),
    ]
