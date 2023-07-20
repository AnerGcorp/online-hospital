# Generated by Django 4.0.8 on 2023-02-06 21:15

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
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('purchased', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PharmacyShop',
            fields=[
                ('pharmacy_shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=1000)),
                ('featured_image', models.ImageField(blank=True, default='pharmacist/user-default.png', null=True, upload_to='pharmacyshop/')),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone_number_1', models.CharField(blank=True, max_length=12, null=True)),
                ('phone_number_2', models.CharField(blank=True, max_length=12, null=True)),
                ('working_hours_start', models.TimeField()),
                ('working_hours_end', models.TimeField()),
                ('working_days', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('pharmacist_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('degree', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_image', models.ImageField(blank=True, default='pharmacist/user-default.png', null=True, upload_to='doctors/')),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(blank=True, max_length=200, null=True)),
                ('trans_ID', models.CharField(blank=True, max_length=200, null=True)),
                ('orderitems', models.ManyToManyField(to='pharmacy.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_number', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('featured_image', models.ImageField(blank=True, default='medicines/default.png', null=True, upload_to='medicines/')),
                ('description', models.TextField(blank=True, null=True)),
                ('medicine_type', models.CharField(blank=True, choices=[('tablets', 'tablets'), ('syrup', 'syrup'), ('capsule', 'capsule'), ('general', 'general')], max_length=200, null=True)),
                ('medicine_category', models.CharField(blank=True, choices=[('fever', 'fever'), ('pain', 'pain'), ('cough', 'cough'), ('cold', 'cold'), ('flu', 'flu'), ('diabetes', 'diabetes'), ('eye', 'eye'), ('ear', 'ear'), ('allergy', 'allergy'), ('asthma', 'asthma'), ('bloodpressure', 'bloodpressure'), ('heartdisease', 'heartdisease'), ('vitamins', 'vitamins'), ('digestivehealth', 'digestivehealth'), ('skin', 'skin'), ('infection', 'infection'), ('nurological', 'nurological')], max_length=200, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('stock_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('prescription_required', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=200, null=True)),
                ('pharmacy_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacyshop')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicine'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
