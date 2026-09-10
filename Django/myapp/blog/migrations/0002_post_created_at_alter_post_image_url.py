# Generated manually for the role-based blog workflow.
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [("blog", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
