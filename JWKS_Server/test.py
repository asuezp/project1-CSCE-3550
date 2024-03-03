import unittest
from JWKS_Server import app

class TestJWKS(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.testing = True

    def test_jwks_endpoint(self):
        response = self.app.get('/.well-known/jwks.json')
        # Assertions go here
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()