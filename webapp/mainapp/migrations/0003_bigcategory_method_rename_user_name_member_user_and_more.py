# Generated by Django 4.1 on 2023-11-10 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_member_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BigCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.BooleanField(help_text='収入ならTrue, 支出ならFalse')),
                ('name', models.CharField(max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='member',
            old_name='user_name',
            new_name='user',
        ),
        migrations.CreateModel(
            name='SmallCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('big_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bigcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.BooleanField(help_text='収入ならTrue, 支出ならFalse')),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
                ('memo', models.TextField()),
                ('member', models.ManyToManyField(to='mainapp.member')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.method')),
                ('small_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.smallcategory')),
            ],
        ),
    ]
