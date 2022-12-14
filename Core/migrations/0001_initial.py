# Generated by Django 4.1.3 on 2022-12-01 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminsExtra",
            fields=[
                ("cargo", models.CharField(max_length=255)),
                ("area", models.CharField(max_length=255)),
                ("vinculo", models.CharField(max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Areas",
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
                ("nome", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Chamados",
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
                ("nome", models.CharField(max_length=255)),
                ("setor", models.CharField(max_length=255)),
                ("titulo", models.CharField(max_length=255)),
                ("descricao", models.CharField(max_length=255)),
                ("prior", models.IntegerField()),
                ("status", models.CharField(max_length=255)),
                ("data", models.DateTimeField(auto_now_add=True)),
                ("areas", models.ManyToManyField(to="Core.areas")),
            ],
        ),
    ]
