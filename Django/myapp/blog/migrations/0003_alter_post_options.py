from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("blog", "0002_post_created_at_alter_post_image_url")]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
    ]
