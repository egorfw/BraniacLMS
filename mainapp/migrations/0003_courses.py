from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    Courses = apps.get_model("mainapp", "Courses")
    # Create model's objects
    Courses.objects.create(
        name="Курс 1",
        description="Информация по Курсу 1",
        cost="10000",
    )
    Courses.objects.create(
        name="Курс 2",
        description="Информация по Курсу 2",
        cost="10000",
    )
    Courses.objects.create(
        name="Курс 3",
        description="Информация по Курсу 3",
        cost="10000",
    )

def reverse_func(apps, schema_editor):
    # Get model
    Courses = apps.get_model("mainapp", "News")
    # Delete objects
    Courses.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]