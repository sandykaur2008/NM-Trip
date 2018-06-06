import unittest 
from app import app, mail


class Routes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        mail.init_app(app)

    def tearDown(self):
        pass
    
    def test_200(self):
        response1 = self.client.get('/')
        response2 = self.client.get('/about')
        response3 = self.client.get('/carlsbad')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
    
    def test_302(self):
        response = self.client.post('/contact', data={
            'text': 'some text',
            'email': 'ex@example.com',
            'name': 'some name'}, follow_redirects=False)
        self.assertEqual(response.status_code, 302)

    def test_404(self):
        response = self.client.get('/doesntexist')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()