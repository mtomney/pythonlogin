from app import app
import unittest

#Test that Flask was properly setup
class FlaskTestCase(unittest.TestCase):
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
	unittest.main()

#Test that the login page properly loads
	def test_login_load(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Please enter login information' in response.data)