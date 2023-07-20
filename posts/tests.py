# from django.test import TestCase, Client
# from django.urls import reverse


# class PostsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
       
#     def tesr_index_view(self):
#         response = self.client.get(reverse("index-page"))
#         exp_data = "Главнвя сраница"
        
#         self.assertEqual(response.content.decode(), exp_data)
#         self.assertEqual(response.status_code, 200)

# class PostsViewsTestCase(TestCase):
#     def test_get_contacts(self):
#         client = Client()
#         response = client.get('/posts/contacts/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content.decode(), "Контакты:0 755 168 204")

#     def test_get_about(self):
#         client = Client()
#         response = client.get('/posts/about/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content.decode(), "О нас:добро пожаловать в наш сайт")
# posts/tests.py
# posts/tests.py

from django.test import TestCase, Client

class PostsViewsTestCase(TestCase):
    def test_get_contacts(self):
        client = Client()
        response = client.get('/posts/contacts/') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Контакты: 0 755 168 204")

    def test_get_about(self):
        client = Client()
        response = client.get('/posts/about/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "О нас: Мы занимаемся сайтом!")

