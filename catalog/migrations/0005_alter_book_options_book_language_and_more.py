# Generated by Django 4.2.11 on 2024-04-20 16:34

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_alter_bookinstance_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ["title", "author"]},
        ),
        migrations.AddField(
            model_name="book",
            name="language",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catalog.language",
            ),
        ),
        migrations.AddConstraint(
            model_name="language",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("name"),
                name="language_name_case_insensitive_unique",
                violation_error_message="Language already exists (case insensitive match)",
            ),
        ),
    ]