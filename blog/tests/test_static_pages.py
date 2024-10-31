from django.test import TestCase
from django.urls import reverse

class StaticPagesTests(TestCase):
  def test_get_home_page(self):
    url = reverse("home")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/home.html')