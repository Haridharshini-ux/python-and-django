from blog.models import post
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Description of your custom command"

    def handle(self, *args, **options):
        title = [
            "post1title",
            "post2title"
        ]
        content = [
            "post1content",
            "post2content"
        ]
        image_url = [
            "https://dummy1",
            "https://dummy2"
        ]
        for title, content, image_url in zip(title, content, image_url):
            post.objects.create(title=title, content=content, image_url=image_url)
        self.stdout.write("Successfully inserted data")
