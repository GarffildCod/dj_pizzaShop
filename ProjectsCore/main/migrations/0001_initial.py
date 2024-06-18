# Generated by Django 4.2 on 2024-06-13 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSite', models.CharField(blank=True, max_length=50, null=True, verbose_name='Названия магазина')),
                ('phoneWork', models.CharField(blank=True, max_length=20, null=True, verbose_name='Рабочий номер телефона')),
                ('emailWork', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Рабочий Email')),
                ('textBanerMain', models.TextField(blank=True, null=True, verbose_name='Текст на главный банер')),
                ('photoBanerMainOne', models.ImageField(blank=True, null=True, upload_to='content', verbose_name='Главный банер 1 ()')),
                ('photoBanerMainTwo', models.ImageField(blank=True, null=True, upload_to='content', verbose_name='Главный банер 2 ()')),
                ('urlDeliveryClub', models.URLField(blank=True, null=True, verbose_name='Ссылка на Delivery Club')),
                ('adressShop', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес магазина')),
                ('ulrWhatsApp', models.URLField(blank=True, null=True, verbose_name='Ссылка на WhatsApp')),
                ('banerLinkShop', models.ImageField(blank=True, null=True, upload_to='content', verbose_name='Банер магазин')),
                ('banerLinkAbout', models.ImageField(blank=True, null=True, upload_to='content', verbose_name='Банер О нас')),
                ('banerLinkContactUs', models.ImageField(blank=True, null=True, upload_to='content', verbose_name='Банер контакты')),
                ('banerDeliveryClubIndex', models.ImageField(blank=True, null=True, upload_to='content', verbose_name='Банер контакты Delivery Club на главной')),
                ('banerAboutContent', models.ImageField(blank=True, null=True, upload_to='content', verbose_name='Банер на страницу "О нас для" описания ')),
            ],
            options={
                'verbose_name': 'Контент на странице',
                'verbose_name_plural': 'Контент на страницах',
            },
        ),
        migrations.CreateModel(
            name='ContentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoCategory', models.ImageField(blank=True, null=True, upload_to='contentCategory', verbose_name='Фото категории')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Категории на главное меню',
                'verbose_name_plural': 'Категории на главное меню',
            },
        ),
    ]
