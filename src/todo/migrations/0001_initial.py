# Generated by Django 3.1.1 on 2020-10-16 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('order_num', models.IntegerField(editable=False)),
                ('slug', models.SlugField(editable=False, max_length=160)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=400)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_important', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('date_completed', models.DateTimeField(null=True)),
                ('category', models.ManyToManyField(to='todo.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('user', 'slug'), name='unique_user_slug'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('user', 'order_num'), name='unique_user_order'),
        ),
    ]
