import unittest 
from app import app


class Routes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def tearDown(self):
        pass
    
    def test_200(self):
        response1 = self.client.get('/')
        response2 = self.client.get('/carlsbad')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_404(self):
        response = self.client.get('/doesntexist')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()