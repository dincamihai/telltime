import unittest
from mock import Mock, patch
from telltime.manage import create_app


def create_mock_app():
    app = create_app()
    return app


class ApiTestCase(unittest.TestCase):

    def setUp(self):
            self.app = create_mock_app()
            #self.addCleanup(app_teardown)
            self.client = self.app.test_client()

    def test_root(self):
        with patch('telltime.telltime.request') as mock_request:
            mock_request.remote_addr = '8.8.8.8'
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
