# Generated by Django 4.2.2 on 2023-07-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0016_alter_commentshop_report_count_commentshopreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopreport',
            name='report_type',
            field=models.CharField(choices=[('Inappropriate Content', 'Inappropriate Content'), ('Fake Shop', 'Fake Shop'), ('Other', 'Other')], max_length=50, null=True),
        ),
    ]
