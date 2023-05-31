# Generated by Django 4.2.1 on 2023-05-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('noq', models.IntegerField()),
                ('duration', models.IntegerField(help_text='duration of the quiz')),
                ('passing_score', models.IntegerField(help_text='required score in %')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('average', 'average'), ('hard', 'hard')], max_length=7)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
    ]