from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):

    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('homepage'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'HOME')

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'pages/home.html')



