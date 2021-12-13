

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprises', '0007_alter_enterprisemodel_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprisemodel',
            name='accepted',
        ),
    ]
