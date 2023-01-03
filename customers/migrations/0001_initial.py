# Generated by Django 3.2 on 2022-12-22 17:55

from django.db import migrations, models
import tenant_schemas.postgresql_backend.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_url', models.CharField(max_length=128, unique=True)),
                ('schema_name', models.CharField(max_length=63, unique=True, validators=[tenant_schemas.postgresql_backend.base._check_schema_name])),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('subdomain', models.CharField(blank=True, default=None, max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('username', models.CharField(max_length=300, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=300)),
                ('address', models.CharField(default=None, max_length=200)),
                ('city', models.CharField(default=None, max_length=200)),
                ('state', models.CharField(default=None, max_length=200)),
                ('country', models.CharField(default=None, max_length=200)),
                ('zipcode', models.CharField(default=None, max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]