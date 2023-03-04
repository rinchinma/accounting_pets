# Generated by Django 4.1.4 on 2022-12-16 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя питомца')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('type', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat')], max_length=3, verbose_name='Вид питомца')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания записи')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='Картинка')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='pets_api.pet')),
            ],
            options={
                'verbose_name': 'Фотография питомца',
                'verbose_name_plural': 'Фотографии питомца',
            },
        ),
    ]