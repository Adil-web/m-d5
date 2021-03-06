# Generated by Django 2.2.6 on 2020-07-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200720_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowbook',
            name='penalties',
            field=models.CharField(choices=[('00%', 'Идеальное состояние'), ('10%', 'Заметные следы'), ('50%', 'Значительное повреждение')], default='00%', max_length=3),
        ),
        migrations.AddField(
            model_name='borrowbook',
            name='returned_flag',
            field=models.BooleanField(default=False),
        ),
    ]
