# Generated by Django 4.2.4 on 2023-09-04 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("currency", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Operation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("OP", "open"), ("LO", "loss"), ("PR", "profit")],
                        max_length=2,
                    ),
                ),
                ("open_datetime", models.DateTimeField()),
                (
                    "close_datetime",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("open_price", models.FloatField()),
                ("close_price", models.FloatField(blank=True, default=None, null=True)),
                ("volume", models.FloatField(default=0.01)),
                ("leverage", models.IntegerField(default=100)),
                (
                    "position",
                    models.CharField(
                        choices=[("LN", "long"), ("SH", "short")],
                        help_text="Operation type, e.g long for buy",
                        max_length=2,
                    ),
                ),
                (
                    "pips",
                    models.FloatField(default=0.0, help_text="Profit/loss in pips"),
                ),
                (
                    "profit",
                    models.FloatField(
                        default=0.0,
                        help_text="In USD Profit/loss of the operation after closed",
                    ),
                ),
                (
                    "currency_pair",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="currency.currencypair",
                    ),
                ),
            ],
        ),
    ]
