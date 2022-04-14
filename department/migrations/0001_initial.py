# Generated by Django 4.0.4 on 2022-04-14 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='название')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=100, verbose_name='имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='отчество')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='employee/', verbose_name='фотография')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='возраст')),
                ('salary', models.PositiveIntegerField(blank=True, null=True, verbose_name='оклад')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_department', to='department.employee'),
        ),
    ]