from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_get(self):
        # TODO some sort of test
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')