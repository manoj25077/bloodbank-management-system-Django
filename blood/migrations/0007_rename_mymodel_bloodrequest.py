# Generated by Django 5.0.3 on 2024-03-21 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_rename_bloodrequest_mymodel_alter_stock_id'),
        ('donor', '0003_alter_blooddonate_id_alter_donor_id'),
        ('patient', '0002_alter_patient_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyModel',
            new_name='BloodRequest',
        ),
    ]