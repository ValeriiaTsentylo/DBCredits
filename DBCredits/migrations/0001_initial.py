# Generated by Django 4.1.1 on 2022-09-20 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuance_date', models.DateField(verbose_name='issuance_date')),
                ('return_date', models.DateField(verbose_name='return_date')),
                ('actual_return_date', models.DateField(verbose_name='actual_return_date')),
                ('body', models.IntegerField(verbose_name='body')),
                ('percent', models.FloatField(verbose_name='percent')),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, verbose_name='login')),
                ('registration_date', models.DateField(verbose_name='registration_date')),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(verbose_name='period')),
                ('sum', models.IntegerField(verbose_name='sum')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DBCredits.dictionary')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='payment_date')),
                ('sum', models.FloatField(verbose_name='sum')),
                ('credit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DBCredits.credits')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DBCredits.dictionary')),
            ],
        ),
        migrations.AddField(
            model_name='credits',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DBCredits.users'),
        ),
    ]
