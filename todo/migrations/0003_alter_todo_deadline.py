# Generated by Django 4.1 on 2022-10-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_todo_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo", name="deadline", field=models.DateField(),
        ),
    ]
