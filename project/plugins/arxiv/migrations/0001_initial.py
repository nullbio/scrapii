# Generated by Django 5.0.6 on 2024-06-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Archive",
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
                ("end_year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="MonthlyArchive",
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
                ("year", models.TextField(max_length=4)),
                ("month", models.TextField(max_length=2)),
                ("total_entries", models.IntegerField()),
                ("scraped_entries", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Paper",
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
                ("title", models.TextField()),
                ("favorite", models.BooleanField(default=False)),
                ("rating", models.FloatField(default=0)),
                ("flag", models.FloatField(default=0)),
                ("page_link", models.TextField(blank=True, null=True, unique=True)),
                ("file_link", models.TextField(blank=True, null=True, unique=True)),
                ("skip_page_download", models.BooleanField(default=False)),
                ("skip_file_download", models.BooleanField(default=False)),
                ("download_failed", models.BooleanField(default=False)),
                ("download_attempt_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("paper_id", models.TextField(unique=True)),
                ("authors", models.TextField(blank=True, null=True)),
                ("summary", models.TextField(blank=True, null=True)),
                ("doi", models.TextField(blank=True, null=True, unique=True)),
                ("related_doi", models.TextField(blank=True, null=True)),
                ("issn", models.TextField(blank=True, null=True)),
                ("report_no", models.TextField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                ("journal_ref", models.TextField(blank=True, null=True)),
                ("published_date", models.DateTimeField(blank=True, null=True)),
                ("updated_date", models.DateTimeField(blank=True, null=True)),
                ("withdrawn", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TotalEntriesMismatch",
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
                ("total_entries", models.IntegerField()),
                ("counted_entries", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
