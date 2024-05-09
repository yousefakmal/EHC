# Generated by Django 3.2.25 on 2024-05-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('feedback', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MessageSender', models.CharField(max_length=50, null=True)),
                ('Message_date', models.DateTimeField(auto_now_add=True)),
                ('Message', models.CharField(max_length=1024, null=True)),
                ('Response', models.CharField(max_length=1024, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='ticket_files/')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_maker', models.CharField(max_length=50, null=True)),
                ('ticket_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('ticket', models.CharField(max_length=1024, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='ticket_files/')),
                ('closed', models.BooleanField(default=False)),
                ('answer', models.CharField(max_length=1024, null=True)),
            ],
        ),
    ]