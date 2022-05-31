from django.test import SimpleTestCase, TestCase


# Create your tests here.
class Simpletest(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        return self.assertEqual(response.status_code, 200)
    
    # def test_productpage(self):
    #     response = self.client.get('/product/')
    #     return self.assertEqual(response.status_code, 200)
    
    def test_add_product_page(self):
      response = self.client.get('/add/')
      return self.assertEqual(response.status_code, 200)