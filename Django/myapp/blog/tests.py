from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RoleAccessTests(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user("customer", password="customer-pass")
        self.admin = User.objects.create_user("editor", password="admin-pass", is_staff=True)

    def test_customer_can_sign_in_and_see_posts(self):
        response = self.client.post(reverse("blog:customer_login"), {"username": "customer", "password": "customer-pass"})
        self.assertRedirects(response, reverse("blog:index"))
        self.assertEqual(self.client.get(reverse("blog:index")).status_code, 200)

    def test_new_customer_can_sign_up(self):
        response = self.client.post(reverse("blog:customer_signup"), {
            "username": "new-customer",
            "password1": "SafePassword123!",
            "password2": "SafePassword123!",
        })
        self.assertRedirects(response, reverse("blog:index"))
        self.assertTrue(User.objects.filter(username="new-customer", is_staff=False).exists())

    def test_customer_cannot_access_admin_dashboard(self):
        self.client.force_login(self.customer)
        response = self.client.get(reverse("blog:admin_dashboard"))
        self.assertRedirects(response, reverse("blog:admin_login") + "?next=" + reverse("blog:admin_dashboard"))

    def test_admin_can_publish_post(self):
        self.client.force_login(self.admin)
        response = self.client.post(reverse("blog:admin_dashboard"), {"title": "A new update", "content": "A useful announcement.", "image_url": ""})
        self.assertRedirects(response, reverse("blog:admin_dashboard"))
        self.assertEqual(self.client.get(reverse("blog:admin_dashboard")).context["posts"].count(), 1)
