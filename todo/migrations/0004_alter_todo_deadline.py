# Generated by Django 4.1 on 2022-10-15 14:56

from django.db import migrations, models
import todo.widget


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_alter_todo_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(verbose_name=todo.widget.datePickerInput),
        ),
    ]
