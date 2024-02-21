from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a text')

    def test_text_contet(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a text')


class HomePageViewTest(TestCase): # new
    def setUp(self):
        Post.objects.create(text='this is another test')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_current_template(self):
        resp = self.client.get(reverse('home')) #reverse sirve para usar el nombre de la url y no la url por si esta
        #llegara a cambiar
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html') #Comprueba si el template usado es correcto

