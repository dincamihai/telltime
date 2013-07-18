import unittest
from telltime.manage import create_app


def create_mock_app():
    app = create_app()
    return app


class ApiTestCase(unittest.TestCase):

    def setUp(self):
            self.app, app_teardown = create_mock_app()
            self.addCleanup(app_teardown)
            self.client = self.app.test_client()

    def test_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
