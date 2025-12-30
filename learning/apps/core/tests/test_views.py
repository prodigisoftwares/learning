from django.test import TestCase
from django.urls import reverse


class TestIndexView(TestCase):
    def test_get_index_view(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")
        self.assertContains(response, "Learning Site")
