# Generated by Django 4.2 on 2024-08-10 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("test_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChildAdmin",
            fields=[
                (
                    "child_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="test_app.child",
                    ),
                ),
            ],
            bases=("test_app.child",),
        ),
        migrations.CreateModel(
            name="ParentAdmin",
            fields=[
                (
                    "parent_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="test_app.parent",
                    ),
                ),
            ],
            bases=("test_app.parent",),
        ),
    ]
