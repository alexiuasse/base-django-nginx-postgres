# Generated by Django 4.1.2 on 2022-10-15 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historic',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fakemodeltest',
            name='test_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.fakemodeltest'),
        ),
        migrations.AddField(
            model_name='addressbr',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddIndex(
            model_name='historic',
            index=models.Index(fields=['content_type', 'object_id'], name='base_histor_content_999e19_idx'),
        ),
        migrations.AddIndex(
            model_name='addressbr',
            index=models.Index(fields=['content_type', 'object_id'], name='base_addres_content_10b562_idx'),
        ),
    ]
