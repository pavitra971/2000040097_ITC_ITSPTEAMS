# Generated by Django 3.2.2 on 2021-06-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSPfrontend', '0009_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='aboutteam',
            field=models.CharField(default='It WAS A REALLY GOOD EXPERIENCE BEING A PART OF THE TEAM ', max_length=500),
        ),
        migrations.AddField(
            model_name='info',
            name='member1email',
            field=models.CharField(default='koi@gmail.com', max_length=122),
        ),
        migrations.AddField(
            model_name='info',
            name='member1name',
            field=models.CharField(default='koi', max_length=122),
        ),
        migrations.AddField(
            model_name='info',
            name='member1phoneno',
            field=models.CharField(default='9016512711', max_length=12),
        ),
        migrations.AddField(
            model_name='info',
            name='member2email',
            field=models.CharField(default='koi@gmail.com', max_length=122),
        ),
        migrations.AddField(
            model_name='info',
            name='member2name',
            field=models.CharField(default='koi', max_length=122),
        ),
        migrations.AddField(
            model_name='info',
            name='member2phoneno',
            field=models.CharField(default='9016512711', max_length=12),
        ),
        migrations.AddField(
            model_name='info',
            name='member3email',
            field=models.CharField(default='koi@gmail.com', max_length=122),
        ),
        migrations.AddField(
            model_name='info',
            name='member3name',
            field=models.CharField(default='koi', max_length=122),
        ),
        migrations.AddField(
            model_name='info',
            name='member3phoneno',
            field=models.CharField(default='9016512711', max_length=12),
        ),
        migrations.AddField(
            model_name='info',
            name='teamleaderemail',
            field=models.CharField(default='koi@gmail.com', max_length=122),
        ),
        migrations.AddField(
            model_name='info',
            name='teamleadername',
            field=models.CharField(default='koi', max_length=122),
        ),
        migrations.AddField(
            model_name='info',
            name='teamleaderphoneno',
            field=models.CharField(default='9016512711', max_length=12),
        ),
        migrations.AddField(
            model_name='info',
            name='teamname',
            field=models.CharField(default='Horizon', max_length=122),
        ),
    ]
