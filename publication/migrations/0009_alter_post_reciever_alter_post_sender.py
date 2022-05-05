# Generated by Django 4.0.3 on 2022-05-05 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0008_alter_post_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reciever',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='publication.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sender',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='outbox', to=settings.AUTH_USER_MODEL),
        ),
    ]