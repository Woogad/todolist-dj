# Generated by Django 4.1 on 2022-10-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0005_alter_todo_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
