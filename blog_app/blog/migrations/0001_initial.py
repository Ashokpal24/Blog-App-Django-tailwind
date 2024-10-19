# Generated by Django 5.1.2 on 2024-10-19 08:46

import blog.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("author", "0001_initial"),
        ("tag", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=255)),
                ("context", models.TextField()),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("published_at", models.DateField(blank=True, null=True)),
                ("is_published", models.BooleanField(default=False)),
                (
                    "featured_image",
                    models.ImageField(upload_to=blog.models.user_directory_path),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles",
                        to="author.author",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="articles", to="tag.tag"
                    ),
                ),
            ],
        ),
    ]
